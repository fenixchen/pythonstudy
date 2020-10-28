# -*- coding:utf-8 -*-

import yaml


def test(document, header=None):
    if header is None:
        print("**" * 50)
    else:
        print('<<' + header + '>>' + '**' * 50)
    print(document)
    print("--" * 50)
    load = yaml.load(document)
    print(type(load))
    print(load)
    print("--" * 50)
    output = yaml.dump(load, default_flow_style=False)
    print(type(output))
    print(output)
    print("**" * 50)


if __name__ == '__main__':
    # dict
    doc = """
        hero:
          hp: 34
          sp: 8
          level: 4
        orc:
          hp: 12
          sp: 0
          level: 2    
    """
    test(doc, 'dict')

    # list
    doc = """    
    - Multimedia
    - Internet
    - Education
    """
    test(doc, 'list')

    # dict + list
    doc = """
    person:
        - name: CCH
        - age: 22
        - red: True
    
    """
    test(doc, 'dict + list')

    # list of list
    doc = """
    -
      - HTML
      - LaTeX
      - SGML
      - VRML
      - XML
      - YAML
    -
      - BSD
      - GNU Hurd
      - Linux  
    """
    test(doc, 'list + list')

    # dict
    doc = """
        base armor class: 0
        base damage: [4,4]
        plus to-hit: 12
        plus to-dam: 16
        plus to-ac: 0    
    """
    test(doc)

    doc = """
        ? !!python/tuple [0,0]
        : The Hero
        ? !!python/tuple [0,1]
        : Treasure
        ? !!python/tuple [1,0]
        : Treasure
        ? !!python/tuple [1,1]
        : The Dragon    
    """
    test(doc)

    doc = """
    - name: PyYAML
      status: 4
      license: MIT
      language: Python
    - name: PySyck
      status: 5
      license: BSD
      language: Python    
    """
    test(doc)

    doc = """
    { str: [15, 17], con: [16, 16], dex: [17, 18], wis: [16, 16], int: [10, 13], chr: [5, 8] }
    """
    test(doc)

    doc = """
plain: Scroll of Remove Curse
single-quoted: 'EASY_KNOW'
double-quoted: "?"
literal: |    # Borrowed from http://www.kersbergen.com/flump/religion.html
  by hjw              ___
     __              /.-.\
    /  )_____________\\  Y
   /_ /=== == === === =\ _\_
  ( /)=== == === === == Y   \
   `-------------------(  o  )
                        \___/
folded: >
  It removes all ordinary curses from all equipped items.
  Heavy or permanent curses are unaffected.    
    """

    test(doc)

    # recusive objects
    doc = """
left hand: &A
  name: The Bastard Sword of Eowyn
  weight: 30
right hand: *A    
    """
    test(doc)

    #tags
    doc = """
boolean: !!bool "true"
integer: !!int "3"
float: !!float "3.14"    
    """
    test(doc)


    # test
    doc = """
name: Tom Smith
age: 37
spouse:
    name: Jane Smith
    age: 25
children:
 - name: Jimmy Smith
   age: 15
 - name1: Jenny Smith
   age1: 12    
    """
    test(doc)