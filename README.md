# Scraping the page names from Wikipedia category hierarchy

<p align='center'>
<img src="https://github.com/SwamiKannan/Scraping_Wikipedia_categories/blob/main/images/category_scrapes.png">
</p>


This git is specially for the purpose of populating a list of pages / categories that can be entered into Wikipedia's [Special Export](https://en.wikipedia.org/wiki/Special:Export) page to request XML files. 

I was in the process of creating an AI assistant for Physics and was trying to download the requisite information from Wikipedia for this purpose. Wikipedia allows us to:
<ol>
  <li> Download all article for a single category say Physics from their <a href="https://en.wikipedia.org/wiki/Special:Export">Special:Export page.</a></li>
  <li> Download an unrelated bunch of pages in a single XML format from their <a href="https://en.wikipedia.org/wiki/Special:Export">Special:Export page.</a></li>
  <li> Download the <a href="https://en.wikipedia.org/wiki/Special:Export/Train"> XML file </a>for the current revision of a single article.</li>
  <li> Just <a href="https://dumps.wikimedia.org/"> download the entire Wikipedia database </a> and parse the entire Wikipedia database.</li>
</ol>
However, I needed, not just the articles that come under the  "Physics" category, but also the articles that come under the subcategories of Physics e.g. the pages under <a href='https://en.wikipedia.org/wiki/Category:Astrophysics'><i>Astrophysics</i></a> or <a href='https://en.wikipedia.org/wiki/Category:Physicists_by_nationality'><i>Physicists by nationality</i></a>, etc. Parsing the whole database and then filtering out the various categories I wanted was troublesome. Hence, this git.


<br>

## How to run the library
### 1. Download the git file
```
git clone https://github.com/SwamiKannan/Scraping_Wikipedia_categories.git
```
### 1. Decide your parameters
1. Get the URL from where you want to scrape the subcategories and pages. This URL must be a **category** page in Wikipedia i.e. URL of the format: **https://en.wikipedia.org/wiki/Category:**
2. Decide on the maximum number of sub-categories you would like to scrape (optional)
3. Decide on the maximum number of page names you would like to extract (optional)
4. Decide on the depth of the category tree that you would like to extract the page names for (depth is explained in the cover image above)

#### Note 1: If you provide (2), (3) and (4), which ever criteria is met first will halt the scraping
#### Note 2: If you do not provide (2) or (3) or (4) above, the script will keep running until all subcategories are exhausted. This is not recommended since within 7 levels of depth, you can go from Physics to Selena Gomez' We Own the Night Tour page as below:
   <p align = "center">
   <img src="https://github.com/SwamiKannan/Scraping_Wikipedia_categories/blob/main/images/depth_gone_wrong.png">
   </p>
### Run the code below:
```
python get_pages.py "<source category page>" -o <output_directory> (optional) -pl <max number of pages to be downloaded> -cl<max number of categories to be downloaded> -d <depth of scraping>
```


