import sqlite3


def insert_member(first_name, last_name, street_address, zip_code, mail, payed_fee):
    conn = sqlite3.connect('member_information.db')
    conn.execute("INSERT INTO MEMBER_INFORMATION (FIRST_NAME, LAST_NAME, STREET_ADDRESS, ZIP_CODE, MAIL, PAYED_FEE) \
VALUES (?,?,?,?,?,?)", (first_name, last_name, street_address, zip_code, mail, payed_fee))
    conn.commit()
    conn.close()

def delete_member_by_name(first_name):
    conn = sqlite3.connect('member_information.db')
    conn.execute("DELETE from MEMBER_INFORMATION where first_name = ?", (first_name,))
    conn.close()

def edit_last_name_by_name(first_name, last_name):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set LAST_NAME = ? where FIRST_NAME = ?", (first_name, last_name))
    conn.commit()
    conn.close()

def edit_street_address_by_name(first_name, street_address):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set STREET_ADDRESS = ? where FIRST_NAME = ?", (first_name, street_address))
    conn.close()

def edit_zip_code_by_name(first_name, zip_code):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set ZIP_CODE = ? where FIRST_NAME = ?", (first_name, zip_code))
    conn.close()

def edit_mail_by_name(first_name, mail):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set MAIL = ? where FIRST_NAME= ?", (first_name, mail))
    conn.close()

def edit_payed_fee_by_name(first_name, payed_fee):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set PAYED_FEE = ? where FIRST_NAME = ?", (first_name, payed_fee))
    conn.close()

def retrieve_members():
    results = []
    conn = sqlite3.connect('member_information.db')
    cursor = conn.execute("SELECT first_name, last_name, street_address, zip_code, mail, payed_fee from MEMBER_INFORMATION")
    # Member records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results

conn = sqlite3.connect('member_information.db')

query = (''' CREATE TABLE IF NOT EXISTS MEMBER_INFORMATION
            (id INTEGER PRIMARY KEY NOT NULL,
            FIRST_NAME   VARC(50) NOT NULL,
            LAST_NAME     VARC(50) NOT NULL,
            STREET_ADDRESS   VARC(50) NOT NULL,
            ZIP_CODE INTEGER NOT NULL,
            MAIL            VARC(50) NOT NULL,
            PAYED_FEE   VARC(50));''')
conn.execute(query)
conn.close()
