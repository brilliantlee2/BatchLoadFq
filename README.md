# BatchLoadFq

A lightweight Python script to batch-read FASTQ/FASTQ.GZ files.  
To avoid loading large FASTQ files into memory at once, this script returns reads in **batches** of size `batch_size`.  

Each read is represented as a `namedtuple` with the following fields:
- `id`: read identifier  
- `seq`: read sequence  
- `q_letter`: quality string  

---

## Features
- Supports **FASTQ** and **FASTQ.GZ** files.  
- Reads data in **batches** to avoid memory overuse.  
- Each batch is a list of `read_tuple` objects.  
- Customizable batch size with `-b` option.  

---

## Example Output

Example when `batch_size=2`.  
The script outputs 5 batches, and each read contains `id`, `seq`, and `q_letter`:

```python
[read_tuple(id='250F302306011_13_3254_9691_218194966_12238_1_10.95',
            seq='CTGAGAGGCATGGCGACCTTATAAGCAGTGGTATCAACGCAGGGGAGGCCTTGCTTGCGGCTGGAGC...',
            q_letter="'*-/2567787988654656988-,,+++,,-:::75544*-((()&&$%*100-,,-*)+..,+))..."),
 read_tuple(id='250F302306011_13_7217_13022_219426469_17878_2_11.63',
            seq='GGCATGGCGACTTTATCGACATGCTACGATCCGACTTTCTGCGTAACATAGCACCTTCCAGTCGGTG...',
            q_letter=")5::7766788('''(.66657776657431(((()*1,323000366521111367:75567333...")]
[read_tuple(id='250F302306011_12_4239_9839_202265667_13811_0_14.27',
            seq='AGAGGCATGGCGACCTTATCGACATGGCTACGATCCGACTTTCTGCGCACCGAGCATCCTTCTCGTA...',
            q_letter=".3:>??A<;:9999200478<<=<==>>?@@>===5/.00047;=<<;78;>=>>><=?>><***:..."),
 read_tuple(id='250F302306011_11_1196_9613_193709619_34445_3_13.78',
            seq='CTGAGCAGTGGTATCAGCGTTAAACCCTGGAGTCAAATCATGTTATTTATTTGATAGTAGCTACAGC...',
            q_letter="&'''(((*+--**//*'&)+/3311100334433345676666676763555543322211233((...")]
...