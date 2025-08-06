import argparse
from src import sql_scanner, xss_scanner, dir_brute, headers_checker

def main():
    parser = argparse.ArgumentParser(description="Web Application Pentest Toolkit")
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--scan', required=True, help='Comma-separated scan types: sql,xss,dir,headers')

    args = parser.parse_args()
    url = args.url
    scan_types = args.scan.split(',')

    if 'sql' in scan_types:
        sql_scanner.scan(url)
    if 'xss' in scan_types:
        xss_scanner.scan(url)
    if 'dir' in scan_types:
        dir_brute.scan(url)
    if 'headers' in scan_types:
        headers_checker.scan(url)

if __name__ == "__main__":
    main()
