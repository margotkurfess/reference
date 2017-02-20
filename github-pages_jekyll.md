# GitHub Pages and Jekyll

I used GitHub Pages and Jekyll to create [my personal blog](https://margotkurfess.github.io/). Here are some of the tools I found useful and some of my main learnings.

-	[GitHub Pages](https://github.com/margotkurfess/reference/blob/master/github-pages_jekyll.md#github-pages)
-	[Jekyll](https://github.com/margotkurfess/reference/blob/master/github-pages_jekyll.md#jekyll)
-	[Markdown](https://github.com/margotkurfess/reference/blob/master/github-pages_jekyll.md#markdown)
-	[Minimalist templates](https://github.com/margotkurfess/reference/blob/master/github-pages_jekyll.md#minimalist-templates)
-	[Customizing your site](https://github.com/margotkurfess/reference/blob/master/github-pages_jekyll.md#customizing-your-site)


## GitHub Pages

**What is GitHub Pages?**

[GitHub Pages](https://help.github.com/articles/what-is-github-pages/) enables you to host a site from a GitHub repository for free.

## Jekyll

**What is Jekyll?**

[Jekyll](https://jekyllrb.com/docs/home/) is the engine behind GitHub Pages and is a static site generator.

**How is it structured?**

-	[Directory structure](https://jekyllrb.com/docs/structure/)

**How do you write posts?**

It is so simple to [write posts using Jekyll](http://jekyllrb.com/docs/posts/). Long story short:

1.	Write your post in markdown in your `_posts` folder
2.	Name the file using the structure `YEAR-MONTH-DAY-title.md`


Jekyll is also great because you can [write drafts first](https://jekyllrb.com/docs/drafts/) and preview what your site looks like before publishing. Simply do the following:

1.	Write your post in markdown in your `_drafts` folder *(without including the date)*
2.	run the command `bundle exec jekyll serve --drafts` in command line

## Markdown

GitHub pages uses markdown for blog posts, which is really intuitive and easy to use. Here are some Markdown syntax guides I found helpful:

-	[Daring Fireball: Markdown syntax](https://daringfireball.net/projects/markdown/syntax#em)
-	[Zendesk: Formatting text with Markdown](https://support.zendesk.com/hc/en-us/articles/203691016-Formatting-text-with-Markdown)

## Minimalist templates

I forked the repo [mmistakes/minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) as the basis for my site for a few reasons:

-	Clean, but not too simple. It is a nice light grey with a sidebar and sharing capabilities for posts. Plus the photo gets a little darker when you hover over it, which is a nice touch.
-	Easily customizable. It is really simple to add things to the sidebar such as links to social media and new pages with a number of layouts to choose from.
-	This is all made possible for someone new to websites by its [great documentation](https://mmistakes.github.io/minimal-mistakes/). Unless you are a whiz with html, css, and general website structure, I believe this is the single most important factor in picking a template.


There are a few other minimalist templates that I stumbled upon that could also be useful:

-	[Jekyll Themes](http://themes.jekyllrc.org/) has a gallery of themes
-	[Indigo](https://github.com/sergiokopplin/indigo) has a simple landing page and nav for blog, etc.

## Customizing your site

There are infinite ways to customize your site, especially if you build your own rather than use a template.

Even when using a template, however, there are a number of relatively easy ways to customize your site. Here are just a few:

-	Update the `config.yml` file to include personal information (description, title) and things like social media links (GitHub, Twitter, LinkedIn)
-	Change the colors in the `css` file to get different header backgrounds, hover colors, fonts, text sizes e.g.
-	Add a favicon. This is a little detail, but it is the little icon that shows up in your browser tab.