# Scraping the Wikipedia category's hierarchy

This git is specially for the purpose of populating a list of pages / categories that can be entered into Wikipedia's [Special Export](https://en.wikipedia.org/wiki/Special:Export) page to request XML files. 

```
python get_pages.py "<source category page>" -o <output_directory> (optional) -pl <max no pages to be downloaded> -cl<max number of categories to be downloaded> -d <depth of scraping>
```
