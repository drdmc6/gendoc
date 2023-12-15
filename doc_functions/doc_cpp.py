def doc_cpp(name_project, dir_input):
    print('--- generating c++ docs ---')

    os.makedirs('doxygen')
    os.chdir('doxygen')

    config_doxyfile = f'''PROJECT_NAME           = "{name_project}"
INPUT                  = "../../{dir_input}"
OUTPUT_DIRECTORY       = "."
RECURSIVE              = YES
VERBATIM_HEADERS       = NO
GENERATE_HTML          = YES
GENERATE_LATEX         = NO'''

    print('creating doxygen file')
    process = subprocess.Popen('doxygen -g', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()

    print('configurating Doxyfile')
    with open('Doxyfile', 'r') as f: file = f.read().split('\n')
    config_doxyfile = config_doxyfile.split('\n')

    for config in config_doxyfile:
        for i, line in enumerate(file):
            if config.split('=')[0] in line:
                file[i] = config

    file = '\n'.join(file)
    with open('Doxyfile', 'w') as f: f.write(file)

    print('making html files')
    process = subprocess.Popen('doxygen Doxyfile', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    os.chdir('..')

    print('--- c++ docs created ---')