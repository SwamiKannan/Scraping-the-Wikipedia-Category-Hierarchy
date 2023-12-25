# Scraping the page names from Wikipedia category hierarchy

<p align='center'>
<img src="https://github.com/SwamiKannan/Scraping_Wikipedia_categories/blob/main/images/category_scrapes.png">
</p>


This git is specially for the purpose of populating a list of pages / categories that can be entered into Wikipedia's [Special Export](https://en.wikipedia.org/wiki/Special:Export) page to request XML files. 

I was in the process of creating an AI assistant for Physics and was trying to download the requisite information from Wikipedia for this purpose. Wikipedia allows us to:
<ul>
  <li> Download all article for a single category say Physics from their <a href="https://en.wikipedia.org/wiki/Special:Export">Special:Export page.</a></li> 

  <li> Download the <a href="https://en.wikipedia.org/wiki/Special:Export/Train"> XML file </a>for the current revision of a single article.</li> ould not collate the list of all the pages / categories I needed to 

```
python get_pages.py "<source category page>" -o <output_directory> (optional) -pl <max no pages to be downloaded> -cl<max number of categories to be downloaded> -d <depth of scraping>
```
