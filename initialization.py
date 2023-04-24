# log reader by R.Hoobakht 1402-02-04 v.0.2.5
from os import remove

keyword_list = list()

# directory of log files path
files_path = str()

# result of search log file path
output_filename = str()

# sign of the write mode
write_mode = str()

# sign of the read mode
read_mode = str()

# and delimiter to search with and logic
delimiter = str()

# less than sign
less_than = str()

# pure file name
fn = str()

# indent line
tab = str()

# if true consider case-sensitive to find the keywords and if false not
case_sensitive = bool()

# if true consider only system and database logs. if false not
db2_log_only = bool()

# sign of the new line
new_line = str()

# dash sign
dash = str()

# show number of log file
index = int()

# line for file name separator
separator = str()

# close 'log' xml tag
close_log_tag = str()

# back-slash sign
back_slash = str()

# represent number one
one = int()

# start message for logs reading operation
start_message = str()

# end message for logs reading operation
end_message = str()


# -------------------------------------------------------------

def log_version():
    return "log reader by R.Hoobakht 1402-02-04 v.0.2.5"


def set_env_variable():
    global files_path
    global output_filename
    global out_file
    global write_mode
    global read_mode
    global delimiter
    global less_than
    global fn
    global tab
    global dash
    global case_sensitive
    global db2_log_only
    global new_line
    global close_log_tag
    global index
    global separator
    global back_slash
    global one
    global end_message
    global start_message

    files_path = "C:/Users/hoobakht/Downloads/log"
    output_filename = "result.xml"
    write_mode = "w"
    read_mode = "r"
    delimiter = "&&"
    less_than = "<"
    fn = ""
    tab = "\t"
    dash = " - "
    case_sensitive = False
    db2_log_only = False
    new_line = '\n'
    close_log_tag = "</log>"
    back_slash = '\\'
    index = 0
    one = 1
    separator = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    end_message = "The End of the log searching ..."
    start_message = tab + log_version() + new_line + tab + "Log reader start ..."


def remove_file(file_name):
    try:
        remove(file_name)
    except FileNotFoundError:
        print(f"remove {file_name}: {file_name} file not found ...")


def write_header(out_file_object):
    out_file_object.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    out_file_object.write(new_line + new_line)
    out_file_object.write("<log>")
    out_file_object.write(new_line + new_line)


# specified keywords to search
# you can use '&&' delimiter to search with and logic
def set_keywords():
    global keyword_list
    keyword_list = [
        "threadTokenId=\"1679482282160\" && 2023-04-24 && 08:08:13",
        # "http://",
        # "https://"
        # "DEADLOCK",
        # "TIMEOUT",
        # "KEY NOT FOUND",
        # "SSL",
        # "DATASOURCE",
        # "SQL STATE",
        # "PRIVILEGE",
        # "GRAMMAR",
        # "CALL JAMSHMA",
        # "DataIntegrityViolationException",
        # "InvalidDataAccessApiUsageException",
        # "DataAccessResourceFailureException",
        # "MethodArgumentNotValidException"
        # "ResourceAccessException"
    ]


def increase_index():
    global index
    index = index + 1


# -------------------------------------------------------------
# -------------------------------------------------------------

# initialize all variables and objects
set_env_variable()

# delete result.xml file if exist
remove_file(output_filename)

# set keywords to search
set_keywords()

out_file = open(output_filename, write_mode)

# crate output file object and write the header to it
write_header(out_file)
