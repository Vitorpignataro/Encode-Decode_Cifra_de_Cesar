import unicodedata

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabetoCifrado = 'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC'

while True:
    print(f'\33[1;36m=*=*=*=*=*=*=*=*\33[1;31mCifra de César\33[m')
    print('\33[1;36m=*=*=*=*=*=*=*=*\33[1;32mEncrypt(1)')
    print('\33[1;36m=*=*=*=*=*=*=*=*\33[1;32mDecrypt(2)')
    print('\33[1;36m=*=*=*=*=*=*=*=*\33[1;32mEncrypt from a file(3)')
    print('\33[1;36m=*=*=*=*=*=*=*=*\33[1;32mDecrypt from a file(4)\33[m\n')
    ch = int(input('Escolha uma opção [1/2/3/4]: '))
    phrashencrypt = ''
    phrashdecrypt = ''
    print()
    if ch == 1:
        phrase = str(input('Digite a frase que deseja criptografar:'))
        cleanerPhrase = unicodedata.normalize("NFD", phrase)
        cleanerPhrase = cleanerPhrase.encode("ascii", "ignore")
        cleanerPhrase = cleanerPhrase.decode("utf-8")
        for i in range(0, len(phrase)):
            for j in range(0, len(alfabeto)):
                if cleanerPhrase[i] == alfabeto[j]:
                    phrashencrypt += alfabetoCifrado[j]
                if cleanerPhrase[i] == ' ':
                    phrashencrypt += ' '
                    break

        print('\33[1;36m$ >\33[1;35m', phrashencrypt.strip())
        break

    if ch == 2:
        Cipherphrase = str(input('Digite a frase que deseja descriptografar:'))

        for i in range(0, len(Cipherphrase)):
            for j in range(0, len(alfabeto)):
                if Cipherphrase[i] == alfabetoCifrado[j]:
                    phrashdecrypt += alfabeto[j]
                if Cipherphrase[i] == ' ':
                    phrashdecrypt += ' '
                    break
        print('\33[1;36m$ > \33[1;35m', phrashdecrypt.strip())
        break

    if ch == 3:
        print('O formato string do caminho para o arquivo deve ser:')
        print('(\33[1;31mWindows\33[m): \33[1;36mC:/Users/Usuario/pathtofile/NomeDoArquivo.txt\33[m ')
        print('(\33[1;31mLinux\33[m): \33[1;36m/home/Usuario/pathtofile/NomeDoArquivo.txt\33[m ')
        print('')
        path2file = str(input('Caminho para o arquivo: '))
        file = open(path2file, 'r', encoding="utf-8")
        phrasefileencrypt = file.read()
        cleanerPhrase = unicodedata.normalize("NFD", phrasefileencrypt)
        cleanerPhrase = cleanerPhrase.encode("ascii", "ignore")
        cleanerPhrase = cleanerPhrase.decode("utf-8")

        for i in range(0, len(phrasefileencrypt)):
            for j in range(0, len(alfabeto)):
                if cleanerPhrase[i] == alfabeto[j]:
                    phrashencrypt += alfabetoCifrado[j]
                if cleanerPhrase[i] == ' ':
                    phrashencrypt += ' '
                    break

        print('\33[1;36m$ >\33[1;35m', phrashencrypt.strip())
        break

    if ch == 4:
        print('O formato string do caminho para o arquivo deve ser:')
        print('(\33[1;31mWindows\33[m): \33[1;36mC:/Users/Usuario/pathtofile/NomeDoArquivo.txt\33[m ')
        print('(\33[1;31mLinux\33[m): \33[1;36m/home/Usuario/pathtofile/NomeDoArquivo.txt\33[m ')
        print('')
        path2file = str(input('Caminho para o arquivo: '))
        file = open(path2file, 'r', encoding="utf-8")
        phrasefiledecrypt = file.read()
        for i in range(0, len(phrasefiledecrypt)):
            for j in range(0, len(alfabeto)):
                if phrasefiledecrypt[i] == alfabetoCifrado[j]:
                    phrashdecrypt += alfabeto[j]
                if phrasefiledecrypt[i] == ' ':
                    phrashdecrypt += ' '
                    break
        print('\33[1;36m$ >\33[1;35m', phrashdecrypt.strip())
        break

