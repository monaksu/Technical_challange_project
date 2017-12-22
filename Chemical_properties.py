#!/usr/bin/python

""""
This is a python module which contains basic functions uses the my_app.py
"""

import sqlite3


def get_data_from_table(chemical_formula=None, color=None, band_gap=None, bangap_lessOrGreat=None):
    """"
    This function includes all database connections to tables
    """
    conn = sqlite3.connect('ChemicalData.db')
    cur = conn.cursor()

    # When no values are passed with function call
    if (chemical_formula == None and color == None and band_gap == None and bangap_lessOrGreat == None):
        cur.execute("SELECT * FROM compounds_bandgap_color")
    # When only compound name value is passed with function call
    elif (chemical_formula != None and color == None and band_gap == None and bangap_lessOrGreat == None):
        cur.execute("SELECT * FROM compounds_bandgap_color WHERE chemical_formula=:chemical_formula",
                    {"chemical_formula": chemical_formula})
    # When only compound color  value is passed with function call
    elif (chemical_formula == None and color != None and band_gap == None and bangap_lessOrGreat == None):
        color = color.lower()
        cur.execute("SELECT * FROM compounds_bandgap_color WHERE color=:color",{"color": color})
    # When only compound band gap value  value is passed with function call
    elif (chemical_formula == None and color == None and band_gap != None and bangap_lessOrGreat == None):
        cur.execute("SELECT * FROM compounds_bandgap_color WHERE band_gap=:band_gap", {"band_gap": band_gap})
    # When  compound name and color  values are passed with function call
    elif (chemical_formula != None and color != None and band_gap == None and bangap_lessOrGreat == None):
        cur.execute("SELECT * FROM compounds_bandgap_color WHERE chemical_formula=:chemical_formula AND color=:color",
                    {"chemical_formula": chemical_formula,"color": color})
    # When  compound name with band gap less than or greater than values are passed with function call
    elif (chemical_formula != None and color == None and band_gap != None and bangap_lessOrGreat != None):
        if (bangap_lessOrGreat.upper() == "LE"):
            cur.execute("SELECT * FROM compounds_bandgap_color WHERE chemical_formula=:chemical_formula AND "
                        "band_gap <= :band_gap  ", {"chemical_formula": chemical_formula, "band_gap": band_gap})
        elif (bangap_lessOrGreat.upper() == "GE"):
            cur.execute("SELECT * FROM compounds_bandgap_color WHERE chemical_formula=:chemical_formula AND"
                        " band_gap >= :band_gap  ",{"chemical_formula": chemical_formula, "band_gap": band_gap})
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def process_database_results_to_display(listoftuples):
    # this function takes list of tuples and convert it to list of dictionary with key - value format for output
    columns = ["chemical_formula", "band_gap", "color"]
    list_of_dictionary = [dict(zip(columns, row)) for row in listoftuples]
    return list_of_dictionary


def select_all_compounds():
    # this function fetch all compounds
    results = get_data_from_table()
    results = process_database_results_to_display(results)
    return results


def select_compound(name):
    # this function fetch given compound by name
    results = get_data_from_table(name,None,None,None)
    results = process_database_results_to_display(results)
    return results


def select_color(color):
    # this function fetch given compounds by color
    results = get_data_from_table(None,color.upper(),None,None)
    results = process_database_results_to_display(results)
    return results


def select_bandgap(band_gap):
    # this function fetch given compounds by band gap
    results = get_data_from_table(None,None,band_gap,None)
    results = process_database_results_to_display(results)
    return results


def select_compound_with_color(name, color):
    # this function fetch given compounds by name and color
    results = get_data_from_table(name, color.upper(), None, None)
    results = process_database_results_to_display(results)
    return results


def select_compound_with_bandgap(name, lessOrgreater, gap):
    # this function fetch given compounds by name and bandgap value
    results = get_data_from_table(name, None, gap, lessOrgreater)
    results = process_database_results_to_display(results)
    return results
