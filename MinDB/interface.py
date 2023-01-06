import sqlite3


def insert_member(id, first_name, last_name, street_address, zip_code, mail, payed_fee):
    conn = sqlite3.connect('member_information.db')
    conn.execute("INSERT INTO MEMBER_INFORMATION (ID, FIRST_NAME, LAST_NAME, STREET_ADDRESS, ZIP_CODE, MAIL, PAYED_FEE) \
VALUES (?,?,?,?,?,?,?)", (id, first_name, last_name, street_address, zip_code, mail, payed_fee))
    conn.commit()
    conn.close()

def delete_member_by_id(id):
    conn = sqlite3.connect('member_information.db')
    conn.execute("DELETE from MEMBER_INFORMATION where ID = ?", (id, 1))
    conn.close()


def edit_last_name_by_id(id, first_name):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set FIRST_NAME = ? where ID = ?", (id, first_name))
    conn.commit()
    conn.close()

def edit_street_address_by_id(id, last_name):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set LAST_NAME = ? where ID = ?", (id, last_name))
    conn.close()

def edit_zip_code_by_id(id, street_address):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set STREET_ADDRESS = ? where ID = ?", (id, street_address))
    conn.close()

def edit_mail_by_id(id, zip_code):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set ZIP_CODE = ? where ID = ?", (id, zip_code))
    conn.close()

def edit_payed_fee_by_id(id, mail):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set MAIL = ? where ID = ?", (id, mail))
    conn.close()
def edit_payed_fee_by_id(id, payed_fee):
    conn = sqlite3.connect('member_information.db')
    conn.execute("UPDATE MEMBER_INFORMATION set PAYED_FEE = ? where ID = ?", (id, payed_fee))
    conn.close()


def retrieve_members():
    results = []
    conn = sqlite3.connect('member_information.db')
    cursor = conn.execute("SELECT id, first_name, last_name, street_address, zip_code, mail, payed_fee from MEMBER_INFORMATION")

    for row in cursor:
        results.append(list(row))
    return results

conn = sqlite3.connect('member_information.db')

query = (''' CREATE TABLE IF NOT EXISTS MEMBER_INFORMATION
            (ID INTEGER PRIMARY KEY NOT NULL,
            FIRST_NAME   VARC(50) NOT NULL,
            LAST_NAME     VARC(50) NOT NULL,
            STREET_ADDRESS   VARC(50) NOT NULL,
            ZIP_CODE INTEGER NOT NULL,
            MAIL            VARC(50) NOT NULL,
            PAYED_FEE   VARC(50));''')
conn.execute(query)
conn.close()
