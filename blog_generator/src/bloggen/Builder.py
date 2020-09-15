import os
from os.path import join, abspath, dirname
import jinja2
import markdown2
import logging
import importlib
import importlib.util
import sys
from shutil import copyfile
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG,format=FORMAT)
class Builder:
    def __init__(self, reference_folder, destination_folder):
        base = abspath(reference_folder)
        destination = abspath(destination_folder)
        self.folders = \
        {
                "base": base,
                "destination":  destination, 
                "templates":  join(base,"templates"),
                "static":     join(base,"static"),
                "content":    join(base,"content"),
                "posts":  join(base,"content","posts"),
                "pages":  join(base,"content","pages")
        }

        self.files = {
                'global_conf':join(self.folders["base"],"conf.py"),
        }

        self.expected_folders = [
                destination_folder,
                join(destination_folder,"static"),
                join(destination_folder,"pages"),
                join(destination_folder,"posts"),
                ]

        self.templates_filepath= [join(self.folders['templates'],f)
                for f in os.listdir(self.folders['templates'])]
        self.post_template = self.find_template(filename="post",type_="post")  
        
    def build_blog(self):
        for folder in self.expected_folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
        for file_ in os.listdir(self.folders["static"]):
            copyfile(join(self.folders["static"],file_),join(self.expected_folders["static"],file_)) 
        self.scope, self.templates = self.build_scope_n_templates()
        self.rendered_templates = self.render_templates()

    def build_scope_n_templates(self):
        scope = {}
        templates = {"post":self.post_template}
        


        conf_spec = importlib.util.spec_from_file_location("conf", self.files['global_conf'])
        conf_module =  importlib.util.module_from_spec(conf_spec)
        conf_spec.loader.exec_module(conf_module)
        sys.modules["conf"] = conf_module
        d = conf_module.__dict__
        scope["global"] = {key: d[key] for key in d 
                                if "__" not in key}

        scope["pages"] = {}
        for page_relativepath in os.listdir(self.folders['pages']):
            page_filename, extension = os.path.splitext(page_relativepath)
            page_fullpath = join(self.folders['pages'], page_relativepath)
            page_template = self.find_template(page_filename, type_="page")
            variables, content = self.read_page_info(page_fullpath,
                                                    type_="page",
                                                    extension_=extension) 
            context  = scope["global"].copy()
            context.update(variables)
            content = markdown2.markdown(jinja2.Template("".join(content)).render(context))
            variables.update({"content":content})

            templates[page_filename] = page_template
            scope["pages"][page_filename] = variables

        scope["posts"] = {}
        for post_relativepath in os.listdir(self.folders['posts']):
            post_filename, extension = os.path.splitext(post_relativepath)
            post_fullpath = join(self.folders['posts'], post_relativepath)
            variables, content = self.read_page_info(post_fullpath,
                                                    type_="post",
                                                    extension_=extension) 
            context  = scope["global"].copy()
            context.update(variables)
            content = markdown2.markdown(jinja2.Template("".join(content)).render(context))
            variables.update({"content":content})
            scope["posts"][page_filename] = variables

        return scope, templates

    def render_templates(self):
        for page_relativepath in os.listdir(self.folders['pages']):
            page_filename, extension = os.path.splitext(page_relativepath)
            page_fullpath = join(self.folders['pages'], page_relativepath)
            destination_filepath = join(self.folders['destination'],f'{page_filename}.html')
            logging.debug(destination_filepath)
            context = self.scope["global"].copy()
            context.update(self.scope["pages"][page_filename])
            with open(destination_filepath,"w") as outf:
                outf.write( self.templates[page_filename].render(context) )

    def find_template(self,filename,type_):
        found = False
        matched_templates = [fp for fp in self.templates_filepath if filename in fp]
        if matched_templates:
            template_filepath = matched_templates[0] 
            return jinja2.Template(open(template_filepath).read()) 
        else:
            print(filename)
            print(self.templates_filepath)
            raise Exception("Could not find template")

    def read_page_info(self, page_fullpath, type_, extension_):
        variables = {}
        contents = []
        with open(page_fullpath) as inpf:
            try: 
                next_line = inpf.__next__()
                while next_line:
                    variable_name, value = next_line.split(":")
                    variables[variable_name.lower()] = value.strip()
                    next_line = inpf.__next__()
            except:
                for content in inpf:
                    contents.append(content)
        return variables, contents                
