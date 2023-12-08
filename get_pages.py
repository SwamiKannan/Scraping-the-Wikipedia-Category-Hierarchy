from file_utils import initiate_file_opens, write_files
from parse_utils import process_no_depth_page, process_depth_page, check_link_format
import settings
import argparse
import sys

args_parser = argparse.ArgumentParser()
args_parser.add_argument('parent_link', help='The parent category page from where the crawling will begin. Such urls '
                                             'should be in the format "https://en.wikipedia.org/wiki/Category:". Refer '
                                             'to the README.md for more details')
args_parser.add_argument('-o', '--output_dir', help='The output directory where the output will be stored.If not '
                                                    'provided, the current directory will be considered the output '
                                                    'directory')
args_parser.add_argument('-pl', '--max_page_limit', help='Max number of page names and links to be outputted. If both '
                                                         'max_page_limit and max_cat_limit are mentioned, then the '
                                                         'crawling will stop when the first limit is hit. If neither '
                                                         'are provided the crawling will continue till all sub '
                                                         'categories and pages are captured ')
args_parser.add_argument('-cl', '--max_cat_limit',
                         help='Max number of category names and links to be outputted.If both '
                              'max_page_limit and max_cat_limit are mentioned, then the '
                              'crawling will stop when the first limit is hit. If neither '
                              'are provided the crawling will continue till all sub '
                              'categories and pages are captured ')

args_parser.add_argument('-d', '--depth',
                         help='Max depth of branches that the crawler will go through i.e from parent to subcategory before crawling is halted.'
                              'e.g. if we want 15 levels of category crawling from the root url, we say -d 15 or  --depth 15')

args = args_parser.parse_args()
url = args.parent_link
output_dir = args.output_dir if args.output_dir else None
mpl = int(args.max_page_limit) if args.max_page_limit else -1
mcl = int(args.max_cat_limit) if args.max_cat_limit else -1
depth = int(args.depth) if args.depth else None

if not url:
    print('Url is not defined')
    sys.exit()
if not url.startswith('https://en.wikipedia.org/wiki/'):
    print('Url provided is not a valid Wikipedia link')
    sys.exit()
if not url.startswith('https://en.wikipedia.org/wiki/Category:'):
    print('Url should be a category link e.g. "https://en.wikipedia.org/wiki/Category:Mathematics"')
    sys.exit()

settings.init()
parent_url = check_link_format(url)
initiate_file_opens(output_dir, parent_url)


def main():
    if not depth:
        process_no_depth_page(url, parent_url, mpl, mcl)
    else:
        process_depth_page(parent_url, depth, parent_url, mpl, mcl)
    write_files()
    for f in [settings.fcn, settings.fcl, settings.fdl, settings.fpl, settings.fpn]:
        f.close()


if __name__ == "__main__":
    main()
