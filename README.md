# BLOG 

Automated generated blog based on the folder blog_generator/inputs

## How to **add** POSTS to the blog ?

For creating a new blog post you need to create a markdown(.md) file in the folder **blog_generator/inputs/content/posts/** following some guidelines.
We recommend copying an already existing post [(here)](https://github.com/Pret-a-LLOD/pret-a-llod.github.io/tree/master/blog_generator/inputs/content/posts) to avoid mistakes.

### 1. The markdown file must have two sections:

  1. variables (anything that is extra information to be used about the blog post). **required variables**:
      - date: must follow format "2019-09-03 14:49:11" "year-month-day hour:minutes:seconds"
      - title: a single line title
      - slug: a single line text separated by "-" instead of spaces " "; we recommend using the title text separated by "-"
      - type: always "post"
      - summary: a single line text summarizing the content of the post 
      
  2. content (markdown/text that will be displayed in the blog as html)
  
  ```
    abc
    cbcd
  ```

2. The filename and the slug variable must be the same.
1. create a markdown file or copy a post already created [here](https://github.com/Pret-a-LLOD/pret-a-llod.github.io/tree/master/blog_generator/inputs/content/posts)

2. name it {nameofthepost}.md


## How to **add** new PAGES to the blog ?


## How to **edit** POSTS to the  ?

