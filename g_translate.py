#!/usr/bin/env python
#
# Author: Mozhdeh Gheini [gheini at isi dot edu]
# Created: 03/20/2019
#
# Given the input file path and source and target languages, writes the
# translations from Google Translate to the output file.

import time
import argparse

from google.cloud import translate


def main():
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('-i', '--input', required=True, help='Input file path')
    p.add_argument('-s', '--source', required=True, help='Source language')
    p.add_argument('-t', '--target', default='en', help='Target language')
    p.add_argument('-o', '--output', default='gt_out.txt', help='Output file path')
    args = vars(p.parse_args())

    translate_client = translate.Client()

    with open(args['input']) as i, open(args['output'], 'w') as o:
        for line in i:
            translation = translate_client.translate(
                line[:-1],
                target_language=args['target'],
                format_='text',
                source_language=args['source'])
            o.write(translation['translatedText'] + '\n')
            time.sleep(0.5)


if __name__ == '__main__':
    main()
