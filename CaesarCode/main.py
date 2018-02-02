# cli.py
import click


@click.group()
def cli():
    pass


@click.command()
# @click.option('--type', '-t', default = 'ct',
#              help = 'The parameter is responsible for specifying the type of program operation. '
#                     'The parameter can take four values: ct - encryption, dct - decryption, '
#                     'crack - hacking, tcrack - hack algorithm test')
@click.option('--text', '-txt', default='HELLO MY CRYPTOFRIEND',
              help='The text with which the operation will be performed')
@click.option('--lang', '-l', default='eng', help='Source language')
@click.option('--key', '-k', default='A', help='Encryption key')
def crypt(text, lang, key):
    print("Шифрование")
    from CaesarCode import crypt
    print(crypt.CRYPTION_CEASAR(text, key, lang))


@click.command()
@click.option('--text', '-txt', default='HELLO MY CRYPTOFRIEND',
              help='The text with which the operation will be performed')
@click.option('--lang', '-l', default='eng', help='Source language')
@click.option('--key', '-k', default='A', help='Decryption key')
def decrypt(text, lang, key):
    print("Дешифрование")
    from CaesarCode import crypt
    print(crypt.CRYPTION_CEASAR(text, key, lang))


@click.command()
@click.option('--text', '-txt', default='HELLO MY CRYPTOFRIEND',
              help='The text with which the operation will be performed')
@click.option('--lang', '-l', default='eng', help='Source language')
@click.option('--type', '-t', default='1', help='Type of Frequency analise: 0-without analise, 1-monogramms, '
                                                '2-bigramms, 3-trigramms, 4-quadgramms')
def crack(text, lang, type):
    print("Взлом")
    from CaesarCode import bruteforce
    print(bruteforce.CRACK_CEASAR(text, lang, type))


@click.command()
@click.option('--text', '-txt', default='HELLO MY CRYPTOFRIEND',
              help='The text with which the operation will be performed')
@click.option('--lang', '-l', default='eng', help='Source language')
@click.option('--type', '-t', default='1', help='Type of Frequency analise: 0-without analise, 1-monogramms, '
                                                '2-bigramms, 3-trigramms, 4-quadgramms')
def testcrack(text, lang, type):
    print("Взлом")
    from CaesarCode import testcrack
    print(testcrack.CRACK_CEASAR(text, lang, type))


cli.add_command(crypt)
cli.add_command(decrypt)
cli.add_command(crack)
cli.add_command(testcrack)

if __name__ == '__main__':
    cli()
