# log reader by R.Hoobakht 1402-02-04 v.0.2.5
from os import scandir

import initialization as init

if __name__ == "__main__":
    print(init.start_message)
    with scandir(init.files_path) as log_files:
        for item in log_files:
            for in_file in log_files:
                input_file = open(in_file, init.read_mode)
                for line in input_file.readlines():
                    if not (init.fn == input_file.name.split(init.back_slash)[init.one]):
                        init.fn = input_file.name.split(init.back_slash)[init.one]
                        init.out_file.write(init.fn + init.new_line)
                        init.out_file.write(init.separator + init.new_line)
                        init.increase_index()
                        print(init.index, init.dash, init.fn)
                    if init.db2_log_only:
                        if not line.strip().startswith("<"):
                            init.out_file.write(init.tab + line + init.new_line)
                        continue
                    if not line.strip().startswith(init.less_than):
                        init.out_file.write(init.tab + line)
                        init.out_file.write(init.new_line)
                        continue
                    for error_item in init.keyword_list:
                        result = False
                        for split_error_item in error_item.split(init.delimiter):
                            if init.case_sensitive:
                                if split_error_item.strip() in line.strip():
                                    result = True
                                else:
                                    result = False
                                    break
                            else:
                                if split_error_item.strip().lower() in line.strip().lower():
                                    result = True
                                else:
                                    result = False
                                    break
                        if result:
                            init.out_file.write(init.tab + line)
                            init.out_file.write(init.new_line)

        # -------------------------------------------------------------

        init.out_file.write(init.new_line)
        init.out_file.write(init.close_log_tag)
        init.out_file.close()
        input_file.close()
        print(init.new_line + init.end_message)
