
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    with open(file_name,"rb") as fp:
        header = fp.read(header_length)
    
    return header


def is_jpeg(file_name):
    
    header = read_header(file_name, len(jpeg_header))
    je_jpg = header == jpeg_header

    return je_jpg


def is_gif(file_name):
    
    header = read_header(file_name, len(gif_header1))
    header1 = read_header(file_name, len(gif_header2))
    je_gif = (header == gif_header1 or header1 == gif_header2)
    
    return je_gif
    


def is_png(file_name):
    
    header = read_header(file_name, len(png_header))
    je_png = header == png_header
    
    return je_png


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except Exception:
        print("Něco se pokazilo.")
    