import os, urllib.request

def name_file(url):

    reverse_url = url[::-1]
    index = reverse_url.find('/')
    reverse_name = reverse_url[0:index]
    name = reverse_name[::-1]
    
    return name
    
        
def install_file(url):

    file = name_file(url)
    
    if not(os.path.exists(file)):
    
        print(f"\nDownloading '{file}' ...")
        urllib.request.urlretrieve(url, file)
        
        print(f"\n✅ Done, '{file}' Successfully Downloaded!")
        print('\n\t...\t...\t...')

if __name__ == '__main__':
    url = input('\nEnter exact file URL to download: ').strip()
    
    install_file(url)
    
