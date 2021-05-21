# Octopart_KiCad_Integration
Populate KiCad fields with Octopart component attributes using Octoparts V4 API with GraphQL. Part data is extracted from KiCad with kifield, the information is processed into an Octopart query with part number and manufacturer, and it is uploaded it to KiCad with kifield.

## Dependencies and Requirements
You would need python 3.6 or later. These can be seen in the `requirements.txt` file and should be easily installed with the following command. I recommend doing this on a venv as that will ensure that you're using functional versions and dependencies without interfering with you computer's current setup. 

```
pip install requirements.txt
```

You will also need to install [kifield](https://xess.com/KiField/docs/_build/singlehtml/index.html) which can be installed with the following code.

```
pip install kifield
```

### Run in command-line interface (CLI)
This program will update component data in a KiCad schematic or project. Effects can be seen in the symlib table. Selected attributes are collected for resistors and capacitors and the specs are added to the KiCad schematic for reference/review/verification of valid part numbers.

Run the following code in your computer's CLI to execute the program.

```
python schematic_update.py -f <KiCadProjectName>.sch
```

If your system requires it, you may have to type `python3` or `pip3`  instead of `python` or `pip` for the program to work. Additional information can be found in the [kifield](https://xess.com/KiField/docs/_build/singlehtml/index.html) documentation as this can be run on a specific schematic file or entire directory. 

### Functionality
Currently, the code is set up to work specifically on capacitors and resistors and populate the KiCad schematic data with the following fields that are extracted from Octopart. 

* Resistors
    * Resistance 
    * Power Rating
    * Case/Package
    * Voltage Rating
    * Tolerance

* Capacitors
    * Capacitance
    * Dielectric
    * Case/Package
    * Voltage Rating
    * Tolerance
    
This data is then organized by the manufacturer and part number, then converted to a dictionary for the graphQL query variable. The query is executed, and the return is stored in a json file called `partlist_file.json`. This can be used to prevent reaching monthly query quota since the query will likely return identical values if successful. This json file is in the format of a nested dictionary and has the desired fields extracted and inserted into KiCad using kifield. 

***Note that before executing your query, you will be asked for your octopart token. This can be stored in an `octopart-token.txt` with a single line or direct user input via the CLI. The token text must in a format similar to `token=xxxxx-xxxxx-xxxx-xxxx-xxxxxxxxxxx`

### Author's Note
This was done in part with my internship at [Benchmark Space Systems](https://www.benchmarkspacesystems.com/) in Burlington, VT for Spring 2021. Thanks!

Jerry