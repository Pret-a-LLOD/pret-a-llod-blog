# BLOG 

Automated generated blog based on the folder blog_generator/inputs

## How to **add** POSTS to the blog ?

For creating a new blog post you need to create a markdown(.md) file in the folder **blog_generator/inputs/content/posts/** following some guidelines.
We recommend copying an already existing post [(here)](https://github.com/Pret-a-LLOD/pret-a-llod.github.io/tree/master/blog_generator/inputs/content/posts) to avoid mistakes.

**- The markdown file must have two sections**

**- The markdown filename must be the same as the slug variable**

### 1. The markdown file must have two sections:

  1. **variables** (anything that is extra information to be used about the blog post). **required variables**:
      - **date**: must follow format "2019-09-27 04:19:01" "year-month-day hour:minutes:seconds"
      - **title**: a single line title
      - **slug**: a single line text separated by "-" instead of spaces " "
      - **type**: always "post"
      - **summary**: a single line text summarizing the content of the post 
      
  2. **content** (markdown/text that will be displayed in the blog as html)
  
  EXAMPLE:
  
  create a file named this-is-the-title-of-my-post.md in **blog_generator/inputs/content/posts/**
  
  **notice there must be a line break between the variables and the content to distinguish both**
  
  ```
    date: 2020-02-30 12:09:55
    title: this is the title of my post
    slug: this-is-the-title-of-my-post
    type: post
    summary: In this post we will discuss about important events of the pret-a-llod project

    This is the content of my post . Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
    Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. 
    
    this is an image for the post ![](../static/logo-cut-final-300x142.png)
    
    Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. 
  ```
  
### 2. The markdown filename must be the same as the slug variable:
make sure the filename and the slug variable inside the file are the same
    
## How to **edit** existing blog POSTS ?
just edit the .md file in the blog_generator/inputs/content/posts/  and commit the changes


## How to **refer** to image and links in the content of a POST ?
![](../static/{image_filename}) for images and [a website](http://website.com)

## How to **upload** an image to be used ?
just add the image file to **blog_generator/inputs/static/**

## How to **add** new PAGES to the blog ?

