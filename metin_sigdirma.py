text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'

def bosluk(text, n):
    x = text.count(' ')
    if x != 0:
        liste = [0 for i in range(x)]
        a, b, c, text_2 = 0, 0, 0, ''
        while a < n:
            liste[b] += 1
            a += 1
            b += 1
            if b == x: b = 0
        for i in text:
            if i == ' ':
                text_2 += i + ' ' * liste[c]
                c += 1
            else: text_2 += i
    else: text_2 = text
    return text_2

def lorem(text, n):
    result = ''
    while True:
        try:
            look = text[n - 1]
        except:
            new = text
            result += new
            break
        else:
            if look != ' ' and text[n] != ' ':
                a = text[:n][::-1].find(' ') 
                text_2 = text[:n - a - 1]
                b = n - len(text_2)
                new = bosluk(text_2, b) + '\n'
                text = text[n - a:]
                result += new
                new = ''
            elif look == ' ':
                text_2 = text[:n - 1]
                new = bosluk(text_2, 1) + '\n'
                text = text[n:]
                result += new
                new = ''
            elif look != ' ' and text[n] == ' ':
                text_2 = text[:n]
                new += text_2 + '\n'
                text = text[n + 1:]
                result += new
                new = ''
    return result

print(lorem(text, 30))