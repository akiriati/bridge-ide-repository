import subprocess
from . import configure

def run_command(view, command):
		file_name = str(view.file_name())
		working_dirs=configure.working_dirs
		project_data = view.window().project_data()
		if project_data and project_data["folders"]:
			working_dirs.append(project_data["folders"][0]["path"])
	
		for working_dir in working_dirs:
			if file_name.startswith(working_dir):
				file_name = file_name[len(working_dir):]

		region = view.sel()[0]

		b_row, _ = view.rowcol(region.begin())
		e_row, _ = view.rowcol(region.end())
		b_row += 1
		e_row += 1

		selected_text = view.substr(region)

		cmd_list = [ configure.bin_file_path , command, "-f", file_name, 
			         "-a", str(b_row), "-z", str(e_row), "-t", selected_text]

		x = subprocess.check_output(cmd_list)