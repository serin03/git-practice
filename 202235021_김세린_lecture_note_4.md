# Lecture note 4
---
```sh
$ pwd
/home/serin
$ ls
Backup  Documents  Lectures  Pictures  Research  Videos  Dataset  Downloads Music  Public  Study  google-cloud-sdk  Desktop  GitHub  OSS  Repositories  Templates miniconda3
$ cd OSS
$ pwd
/home/serin/OSS
$ ls
neuralintlab transformers
$ cd ..
$ pwd
/home/serin
$ cd OSS/transformers
$ pwd
/home/serin/OSS/transformers
$ ls
README.md  classification_experiment.py  module.py
# cd ../neuralintlab
$ ls
README.md
$ cd /home/serin/OSS/tranformers
$ cp module.py backup_module.py
$ ls
README.md  backup_module.py  classification_experiment.py  module.py
$ cp -r ../neuralintlab .
$ ls
README.md  backup_module.py  classification_experiment.py  module.py  neuralintlab
$ cd neuralintlab
$ ls
README.md
$ pwe
/home/serin/OSS/transformers/neuralintlab
$ cd ..
$ pwd
/home/serin/OSS/transformers
$ ls
README.md  backup_module.py  classification_experiment.py  module.py  neuralintlab
$ mv module.py new_module.py
$ ls
README.md  backup_module.py  classification_experiment.py  module.py  neuralintlab new_module.py
$ mv new_module.py ../neuralintlab
$ cd ../neuralintlab
$ ls
README.md  new_module.py
$ cd ../transformers
$ mv neuralintlab nil
$ ls
README.md  backup_module.py  classification_experiment.py  nil
$ rm backup_module.py
$ ls
README.md  classification_experiment.py  nil
$ ls
neuralintlab  transformers
$ mkdir new_directory
$ ls
neuralintlab  transformers  new_directory
```
---