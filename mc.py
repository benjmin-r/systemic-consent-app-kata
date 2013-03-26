#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import sys
import os

class ModeratorClient(object):
    """
    Repräsentiert den Moderator Client
    """
    
    def __init__(self, output, choices_reader, choices_printer):
        self.choices_reader = choices_reader
        self.output = output
        self.choices_printer = choices_printer
        
        choices = self.choices_reader.read_choices()
        self.choices_printer.print_choices(choices)
        
        # Next: Jetzt alles anzeigen: Publish oder Exit
    
    def start_server(self):
        """
        Starte den Server
        """
        pass
    
class ChoicesPrinter(object):
    """
    Kümmert sich um die saubere Anzeige der Choices
    """
    def __init__(self, output):
        self.output = output
        
    def print_choices(self, choices):
        self.output.write("%d Optionen …" % len(choices))
        self.output.write(os.linesep)
    
class ChoicesReader(object):
    """
    Liest die Optionen ein.
    """
    def __init__(self, input, output):
        self.input = input;
        self.output = output;
        
    def read_choices(self):
        """
        Erfasst die Optionen
        """
        choices = []
        self.output.write("Bitte gib deine Optionen ein (Enter zum Beenden).")
        self.output.write(os.linesep)
        next = True
        while next:
            c = self.read_choice()
            if c == None:
                next = False
            else:
                choices.append(c)
        return choices
    
    def read_choice(self):
        """
        Liest eine Option ein.
        """
        choice = self.input.readline()
        if choice == os.linesep:
            return None
        return choice


if __name__ == "__main__":
    sys.stdout.write("Starting moderator client …" + os.linesep)
    
    input = sys.stdin
    output = sys.stdout
    mc = ModeratorClient(output, ChoicesReader(input, output), ChoicesPrinter(output))
 