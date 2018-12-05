import pdb
#http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html ref


HEADER = """
COLUMNS       DATA  TYPE     FIELD             DEFINITION
------------------------------------------------------------------------------------
 1 -  6       Record name    "HEADER"
11 - 50       String(40)     classification    Classifies the molecule(s).
51 - 59       Date           depDate           Deposition date. This is the date the
                                               coordinates  were received at the PDB.
63 - 66       IDcode         idCode            This identifier is unique within the PDB.
"""


TITLE = """
COLUMNS       DATA  TYPE     FIELD         DEFINITION
----------------------------------------------------------------------------------
 1 -  6       Record name    "TITLE "
 9 - 10       Continuation   continuation  Allows concatenation of multiple records.
11 - 80       String         title         Title of the  experiment.
"""

COMPND = """
COLUMNS       DATA TYPE       FIELD         DEFINITION
----------------------------------------------------------------------------------
 1 -  6       Record name     "COMPND"  
 8 - 10       Continuation    continuation  Allows concatenation of multiple records.
11 - 80       Specification   compound      Description of the molecular components.
              list  
"""


SOURCE = """
COLUMNS      DATA  TYPE     FIELD          DEFINITION                       
--------------------------------------------------------------------------------------
 1 -  6      Record name    "SOURCE"      
 8 - 10      Continuation   continuation   Allows concatenation of multiple records.
11 - 79      Specification  srcName        Identifies the source of the
             List                          macromolecule in a  token: value format.
"""


KEYWDS = """
COLUMNS       DATA  TYPE     FIELD         DEFINITION 
---------------------------------------------------------------------------------
 1 -  6       Record name    "KEYWDS" 
 9 - 10       Continuation   continuation  Allows concatenation of records if necessary.
11 - 79       List           keywds        Comma-separated list of keywords relevant
                                           to the entry.   
"""

EXPDTA = """
COLUMNS       DATA TYPE      FIELD         DEFINITION   
------------------------------------------------------------------------------------
 1 -  6       Record name    "EXPDTA"  
 9 - 10       Continuation   continuation  Allows concatenation of multiple records.
11 - 79       SList          technique     The experimental technique(s) with 
                                           optional comment describing the
                                           sample or experiment.
"""

AUTHOR = """
COLUMNS      DATA  TYPE      FIELD         DEFINITION                          
------------------------------------------------------------------------------------
 1 -  6      Record name     "AUTHOR"                                            
 9 - 10      Continuation    continuation  Allows concatenation of multiple records.
11 - 79      List            authorList    List of the author names, separated   
                                           by commas.
"""

REVDAT = """
COLUMNS       DATA  TYPE     FIELD         DEFINITION                            
-------------------------------------------------------------------------------------
 1 -  6       Record name    "REVDAT"                                            
 8 - 10       Integer        modNum        Modification number.                  
11 - 12       Continuation   continuation  Allows concatenation of multiple records.
14 - 22       Date           modDate       Date of modification (or release  for  
                                           new entries)  in DD-MMM-YY format. This is
                                           not repeated on continued lines.
24 - 27       IDCode         modId         ID code of this entry. This is not repeated on
                                           continuation lines.   
32            Integer        modType       An integer identifying the type of   
                                           modification. For all  revisions, the
                                           modification type is listed as 1
40 - 45       LString(6)     record        Modification detail.
47 - 52       LString(6)     record        Modification detail.
54 - 59       LString(6)     record        Modification detail.
61 - 66       LString(6)     record        Modification detail.
"""

JRNL = """
COLUMNS       DATA TYPE      FIELD         DEFINITION                 
-----------------------------------------------------------------------
 1 -  6       Record name    "JRNL"                                 
13 - 79       LString        text          See Details below.       
"""

REMARK = """
COLUMNS       DATA TYPE     FIELD         DEFINITION
--------------------------------------------------------------------------------------
 1 -  6       Record name   "REMARK"
 8 - 10       Integer       remarkNum     Remark  number. It is not an error for
                                          remark n to exist in an entry when
                                          remark n-1 does not.
12 - 79       LString       empty         Left  as white space in first line
                                          of each  new remark.
"""

DBREF = """
COLUMNS       DATA TYPE     FIELD              DEFINITION
-----------------------------------------------------------------------------------
 1 -  6       Record name   "DBREF "
 8 - 11       IDcode        idCode             ID code of this entry.
13            Character     chainID            Chain  identifier.
15 - 18       Integer       seqBegin           Initial sequence number of the
                                               PDB sequence segment.
19            AChar         insertBegin        Initial  insertion code of the
                                               PDB  sequence segment.
21 - 24       Integer       seqEnd             Ending sequence number of the
                                               PDB  sequence segment.
25            AChar         insertEnd          Ending insertion code of the
                                               PDB  sequence segment.
27 - 32       LString       database           Sequence database name.
34 - 41       LString       dbAccession        Sequence database accession code.
43 - 54       LString       dbIdCode           Sequence  database identification code.
56 - 60       Integer       dbseqBegin         Initial sequence number of the
                                               database seqment.
61            AChar         idbnsBeg           Insertion code of initial residue of the
                                               segment, if PDB is the reference.
63 - 67       Integer       dbseqEnd           Ending sequence number of the
                                               database segment.
68            AChar         dbinsEnd           Insertion code of the ending residue of
                                               the segment, if PDB is the reference.
"""

SEQADV = """
COLUMNS        DATA TYPE     FIELD         DEFINITION
-----------------------------------------------------------------
 1 -  6        Record name   "SEQADV"
 8 - 11        IDcode        idCode        ID  code of this entry.
13 - 15        Residue name  resName       Name of the PDB residue in conflict.
17             Character     chainID       PDB  chain identifier.
19 - 22        Integer       seqNum        PDB  sequence number.
23             AChar         iCode         PDB insertion code.
25 - 28        LString       database
30 - 38        LString       dbAccession   Sequence  database accession number.
40 - 42        Residue name  dbRes         Sequence database residue name.
44 - 48        Integer       dbSeq         Sequence database sequence number.
50 - 70        LString       conflict      Conflict comment.
"""

SEQRES = """
COLUMNS        DATA TYPE      FIELD        DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name    "SEQRES"
 8 - 10        Integer        serNum       Serial number of the SEQRES record for  the
                                           current  chain. Starts at 1 and increments
                                           by one  each line. Reset to 1 for each chain.
12             Character      chainID      Chain identifier. This may be any single
                                           legal  character, including a blank which is
                                           is  used if there is only one chain.
14 - 17        Integer        numRes       Number of residues in the chain.
                                           This  value is repeated on every record.
20 - 22        Residue name   resName      Residue name.
24 - 26        Residue name   resName      Residue name.
28 - 30        Residue name   resName      Residue name.
32 - 34        Residue name   resName      Residue name.
36 - 38        Residue name   resName      Residue name.
40 - 42        Residue name   resName      Residue name.
44 - 46        Residue name   resName      Residue name.
48 - 50        Residue name   resName      Residue name.
52 - 54        Residue name   resName      Residue name.
56 - 58        Residue name   resName      Residue name.
60 - 62        Residue name   resName      Residue name.
64 - 66        Residue name   resName      Residue name.
68 - 70        Residue name   resName      Residue name.
"""


HET = """
COLUMNS       DATA  TYPE     FIELD         DEFINITION
---------------------------------------------------------------------------------
 1 -  6       Record name   "HET   "
 8 - 10       LString(3)    hetID          Het identifier, right-justified.
13            Character     ChainID        Chain  identifier.
14 - 17       Integer       seqNum         Sequence  number.
18            AChar         iCode          Insertion  code.
21 - 25       Integer       numHetAtoms    Number of HETATM records for the group
                                           present in the entry.
31 - 70       String        text           Text describing Het group.
"""

HETNAM = """
COLUMNS       DATA  TYPE    FIELD           DEFINITION
----------------------------------------------------------------------------
 1 -  6       Record name   "HETNAM"
 9 - 10       Continuation  continuation    Allows concatenation of multiple records.
12 - 14       LString(3)    hetID           Het identifier, right-justified.
16 - 70       String        text            Chemical name.
"""

HETSYN = """
COLUMNS       DATA TYPE     FIELD          DEFINITION
----------------------------------------------------------------------------
 1 -  6       Record name   "HETSYN"
 9 - 10       Continuation  continuation   Allows concatenation of multiple records.
12 - 14       LString(3)    hetID          Het identifier, right-justified.
16 - 70       SList         hetSynonyms    List of synonyms.
"""

FORMUL = """
COLUMNS        DATA TYPE     FIELD         DEFINITION
-----------------------------------------------------------------------
 1 -  6        Record name   "FORMUL"
 9 - 10        Integer       compNum       Component  number.
13 - 15        LString(3)    hetID         Het identifier.
17 - 18        Integer       continuation  Continuation number.
19             Character     asterisk      "*" for water.
20 - 70        String        text          Chemical formula.
"""


HELIX = """
COLUMNS        DATA  TYPE     FIELD         DEFINITION
-----------------------------------------------------------------------------------
 1 -  6        Record name    "HELIX "
 8 - 10        Integer        serNum        Serial number of the helix. This starts
                                            at 1  and increases incrementally.
12 - 14        LString(3)     helixID       Helix  identifier. In addition to a serial
                                            number, each helix is given an 
                                            alphanumeric character helix identifier.
16 - 18        Residue name   initResName   Name of the initial residue.
20             Character      initChainID   Chain identifier for the chain containing
                                            this  helix.
22 - 25        Integer        initSeqNum    Sequence number of the initial residue.
26             AChar          initICode     Insertion code of the initial residue.
28 - 30        Residue  name  endResName    Name of the terminal residue of the helix.
32             Character      endChainID    Chain identifier for the chain containing
                                            this  helix.
34 - 37        Integer        endSeqNum     Sequence number of the terminal residue.
38             AChar          endICode      Insertion code of the terminal residue.
39 - 40        Integer        helixClass    Helix class (see below).
41 - 70        String         comment       Comment about this helix.
72 - 76        Integer        length        Length of this helix.
"""

SHEET = """
COLUMNS       DATA  TYPE     FIELD          DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name   "SHEET "
 8 - 10        Integer       strand         Strand  number which starts at 1 for each
                                            strand within a sheet and increases by one.
12 - 14        LString(3)    sheetID        Sheet  identifier.
15 - 16        Integer       numStrands     Number  of strands in sheet.
18 - 20        Residue name  initResName    Residue  name of initial residue.
22             Character     initChainID    Chain identifier of initial residue 
                                            in strand. 
23 - 26        Integer       initSeqNum     Sequence number of initial residue
                                            in strand.
27             AChar         initICode      Insertion code of initial residue
                                            in  strand.
29 - 31        Residue name  endResName     Residue name of terminal residue.
33             Character     endChainID     Chain identifier of terminal residue.
34 - 37        Integer       endSeqNum      Sequence number of terminal residue.
38             AChar         endICode       Insertion code of terminal residue.
39 - 40        Integer       sense          Sense of strand with respect to previous
                                            strand in the sheet. 0 if first strand,
                                            1 if  parallel,and -1 if anti-parallel.
42 - 45        Atom          curAtom        Registration.  Atom name in current strand.
46 - 48        Residue name  curResName     Registration.  Residue name in current strand
50             Character     curChainId     Registration. Chain identifier in
                                            current strand.
51 - 54        Integer       curResSeq      Registration.  Residue sequence number
                                            in current strand.
55             AChar         curICode       Registration. Insertion code in
                                            current strand.
57 - 60        Atom          prevAtom       Registration.  Atom name in previous strand.
61 - 63        Residue name  prevResName    Registration.  Residue name in
                                            previous strand.
65             Character     prevChainId    Registration.  Chain identifier in
                                            previous  strand.
66 - 69        Integer       prevResSeq     Registration. Residue sequence number
                                            in previous strand.
70             AChar         prevICode      Registration.  Insertion code in
                                            previous strand.
"""

SITE = """
COLUMNS        DATA  TYPE    FIELD         DEFINITION
---------------------------------------------------------------------------------
 1 -  6        Record name   "SITE  "
 8 - 10        Integer       seqNum        Sequence number.
12 - 14        LString(3)    siteID        Site name.
16 - 17        Integer       numRes        Number of residues that compose the site.
19 - 21        Residue name  resName1      Residue name for first residue that 
                                           creates the site.
23             Character     chainID1      Chain identifier for first residue of site.
24 - 27        Integer       seq1          Residue sequence number for first residue
                                           of the  site.
28             AChar         iCode1        Insertion code for first residue of the site.
30 - 32        Residue name  resName2      Residue name for second residue that 
                                           creates the site.
34             Character     chainID2      Chain identifier for second residue of
                                           the  site.
35 - 38        Integer       seq2          Residue sequence number for second
                                           residue of the site.
39             AChar         iCode2        Insertion code for second residue
                                           of the  site.
41 - 43        Residue name  resName3      Residue name for third residue that 
                                           creates  the site.
45             Character     chainID3      Chain identifier for third residue
                                           of the site.
46 - 49        Integer       seq3          Residue sequence number for third
                                           residue of the site.
50             AChar         iCode3        Insertion code for third residue
                                           of the site.
52 - 54        Residue name  resName4      Residue name for fourth residue that 
                                           creates  the site.
56             Character     chainID4      Chain identifier for fourth residue
                                           of the site.
57 - 60        Integer       seq4          Residue sequence number for fourth
                                           residue of the site.
61             AChar         iCode4        Insertion code for fourth residue
                                           of the site.
"""

CRYST1 = """
COLUMNS       DATA  TYPE    FIELD          DEFINITION
-------------------------------------------------------------
 1 -  6         Record name   "CRYST1"
 7 - 15         Real(9.3)     a              a (Angstroms).
16 - 24         Real(9.3)     b              b (Angstroms).
25 - 33         Real(9.3)     c              c (Angstroms).
34 - 40         Real(7.2)     alpha          alpha (degrees).
41 - 47         Real(7.2)     beta           beta (degrees).
48 - 54         Real(7.2)     gamma          gamma (degrees).
56 - 66         LString       sGroup         Space  group.
67 - 70         Integer       z              Z value.
"""


ORIGX1 = """
COLUMNS        DATA  TYPE     FIELD         DEFINITION
----------------------------------------------------------------
 1 -  6         Record name   "ORIGX1"      n=1
11 - 20         Real(10.6)    o[1][1]       O11
21 - 30         Real(10.6)    o[1][2]       O12
31 - 40         Real(10.6)    o[1][3]       O13
46 - 55         Real(10.5)    t[1]          T1
"""
ORIGX2 = """
COLUMNS        DATA  TYPE     FIELD         DEFINITION
----------------------------------------------------------------
 1 -  6         Record name   "ORIGX2"     	n=2
11 - 20         Real(10.6)    o[2][1]       O21
21 - 30         Real(10.6)    o[2][2]       O22
31 - 40         Real(10.6)    o[2][3]       O23
46 - 55         Real(10.5)    t[2]          T2
"""
ORIGX3 = """
COLUMNS        DATA  TYPE     FIELD         DEFINITION
----------------------------------------------------------------
 1 -  6         Record name   "ORIGX3"      n=3
11 - 20         Real(10.6)    o[3][1]       O31
21 - 30         Real(10.6)    o[3][2]       O32
31 - 40         Real(10.6)    o[3][3]       O33
46 - 55         Real(10.5)    t[3]          T3
"""

SCALE1 = """
COLUMNS         DATA  TYPE    FIELD              DEFINITION
------------------------------------------------------------------
 1 -  6         Record name   "SCALE1" 		     n=1
11 - 20         Real(10.6)    s[1][1]            S11
21 - 30         Real(10.6)    s[1][2]            S12
31 - 40         Real(10.6)    s[1][3]            S13
46 - 55         Real(10.5)    u[1]               U1
"""

SCALE2 = """
COLUMNS         DATA  TYPE    FIELD              DEFINITION
------------------------------------------------------------------
 1 -  6         Record name   "SCALE2" 		     n=2
11 - 20         Real(10.6)    s[2][1]            S21
21 - 30         Real(10.6)    s[2][2]            S22
31 - 40         Real(10.6)    s[2][3]            S23
46 - 55         Real(10.5)    u[2]               U2
"""
SCALE3 = """
COLUMNS         DATA  TYPE    FIELD              DEFINITION
------------------------------------------------------------------
 1 -  6         Record name   "SCALE3" 		     n=3
11 - 20         Real(10.6)    s[3][1]            S31
21 - 30         Real(10.6)    s[3][2]            S32
31 - 40         Real(10.6)    s[3][3]            S33
46 - 55         Real(10.5)    u[3]               U3
"""

ATOM = """
COLUMNS        DATA  TYPE    FIELD        DEFINITION
-------------------------------------------------------------------------------------
 1 -  6        Record name   "ATOM  "
 7 - 11        Integer       serial       Atom  serial number.
13 - 16        Atom          name         Atom name.
17             Character     altLoc       Alternate location indicator.
18 - 20        Residue name  resName      Residue name.
22             Character     chainID      Chain identifier.
23 - 26        Integer       resSeq       Residue sequence number.
27             AChar         iCode        Code for insertion of residues.
31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
55 - 60        Real(6.2)     occupancy    Occupancy.
61 - 66        Real(6.2)     tempFactor   Temperature  factor.
77 - 78        LString(2)    element      Element symbol, right-justified.
79 - 80        LString(2)    charge       Charge  on the atom.
"""

TER = """
COLUMNS        DATA  TYPE    FIELD           DEFINITION
-------------------------------------------------------------------------
 1 -  6        Record name   "TER   "
 7 - 11        Integer       serial          Serial number.
18 - 20        Residue name  resName         Residue name.
22             Character     chainID         Chain identifier.
23 - 26        Integer       resSeq          Residue sequence number.
27             AChar         iCode           Insertion code.
"""


HETATM = """ 
COLUMNS       DATA  TYPE     FIELD         DEFINITION
-----------------------------------------------------------------------
 1 -  6        Record name    "HETATM"
 7 - 11        Integer        serial        Atom serial number.
13 - 16        Atom           name          Atom name.
17             Character      altLoc        Alternate location indicator.
18 - 20        Residue name   resName       Residue name.
22             Character      chainID       Chain identifier.
23 - 26        Integer        resSeq        Residue sequence number.
27             AChar          iCode         Code for insertion of residues.
31 - 38        Real(8.3)      x             Orthogonal coordinates for X.
39 - 46        Real(8.3)      y             Orthogonal coordinates for Y.
47 - 54        Real(8.3)      z             Orthogonal coordinates for Z.
55 - 60        Real(6.2)      occupancy     Occupancy.
61 - 66        Real(6.2)      tempFactor    Temperature factor.
77 - 78        LString(2)     element       Element symbol; right-justified.
79 - 80        LString(2)     charge        Charge on the atom.
"""

CONECT = """
COLUMNS       DATA  TYPE      FIELD        DEFINITION
-------------------------------------------------------------------------
 1 -  6        Record name    "CONECT"
 7 - 11        Integer        serial       Atom  serial number
12 - 16        Integer        serial       Serial number of bonded atom
17 - 21        Integer        serial       Serial  number of bonded atom
22 - 26        Integer        serial       Serial number of bonded atom
27 - 31        Integer        serial       Serial number of bonded atom
"""

MASTER = """
COLUMNS         DATA TYPE     FIELD          DEFINITION
----------------------------------------------------------------------------------
 1 -  6         Record name   "MASTER"
11 - 15         Integer       numRemark      Number of REMARK records
16 - 20         Integer       "0"
21 - 25         Integer       numHet         Number of HET records
26 - 30         Integer       numHelix       Number of HELIX records
31 - 35         Integer       numSheet       Number of SHEET records
36 - 40         Integer       numTurn        deprecated
41 - 45         Integer       numSite        Number of SITE records
46 - 50         Integer       numXform       Number of coordinate transformation
                                             records  (ORIGX+SCALE+MTRIX)
51 - 55         Integer       numCoord       Number of atomic coordinate records
                                             records (ATOM+HETATM)
56 - 60         Integer       numTer         Number of TER records
61 - 65         Integer       numConect      Number of CONECT records
66 - 70         Integer       numSeq         Number of SEQRES records
"""

END = """
COLUMNS         DATA TYPE     FIELD          DEFINITION
----------------------------------------------------------------------------------
 1 -  6         Record name   "MASTER"
11 - 15         Integer       numRemark      Number of REMARK records
16 - 20         Integer       "0"
21 - 25         Integer       numHet         Number of HET records
26 - 30         Integer       numHelix       Number of HELIX records
31 - 35         Integer       numSheet       Number of SHEET records
36 - 40         Integer       numTurn        deprecated
41 - 45         Integer       numSite        Number of SITE records
46 - 50         Integer       numXform       Number of coordinate transformation
                                             records  (ORIGX+SCALE+MTRIX)
51 - 55         Integer       numCoord       Number of atomic coordinate records
                                             records (ATOM+HETATM)
56 - 60         Integer       numTer         Number of TER records
61 - 65         Integer       numConect      Number of CONECT records
66 - 70         Integer       numSeq         Number of SEQRES records
"""

#COLUMNS        DATA  TYPE    FIELD        DEFINITION
#none of the fixed width parsers worked so make my own
def fixedWidth(text, splitVals):
	#get header
	#skip ----
	val0 = 0 # start of line
	lines = text.split('\n')[2:]:
	# val1  = pos of beginning of record name
	val1 = lines[0].find("Record ")

	# val 2 = begining of field 
	# val 3 beginning of definition line 4
	#get nums to split on , not consistent, 1-6 record name is consistent
	#need to definition split value from line 3 

	
"""
def writeExcel(llDict, fileName):
	dictKey = "Null RN "
	print("writing " , dictKey)
"""
#@headerString = "COLUMNS        DATA  TYPE    FIELD        DEFINITION"
# Found headers
# ['HEADER', 'TITLE', 'COMPND', 'SOURCE', 'KEYWDS', 'EXPDTA', 'AUTHOR', 'REVDAT', 'JRNL', 'REMARK', 'DBREF', 'SEQADV', 'SEQRES', 'HET', 'HETNAM', 'HETSYN', 'FORMUL', 'HELIX', 'SHEET', 'SITE', 'CRYST1', 'ORIGX1', 'ORIGX2', 'ORIGX3', 'SCALE1', 'SCALE2', 'SCALE3', 'ATOM', 'TER', 'HETATM', 'CONECT', 'MASTER', 'END']
# todo count occurences for speeeed
if __name__ == "__main__":

	#DATA:  15  FIELD:  29  DEFINITION:  42
	tableList=[HEADER, TITLE, COMPND, SOURCE, KEYWDS, EXPDTA, AUTHOR, REVDAT, JRNL, REMARK, DBREF, SEQADV, SEQRES, HET, HETNAM, HETSYN, FORMUL, HELIX, SHEET, SITE, CRYST1, ORIGX1, ORIGX2, ORIGX3, SCALE1, SCALE2, SCALE3, ATOM, TER, HETATM, CONECT, MASTER, END]
	firstWord = []
	for line in open("2p4y.pdb", "r"):
		if line.split()[0] not in firstWord:
			firstWord.append(line.split()[0])

	print(firstWord)
	#print("DATA: ", headerString.find("DATA"), " FIELD: ", headerString.find("FIELD"),  " DEFINITION: ", headerString.find("DEFINITION"))
	