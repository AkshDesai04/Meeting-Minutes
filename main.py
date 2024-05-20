import ingest
import data_cleanup
import process_texts

def main():
    # file_path = input("Enter file path")
    file_path = 'test.txt'
    # file_path = './Meeting-Minutes/test.txt'
    file_content = ingest.ingest_target(file_path)
    file_content = data_cleanup.master_cleanup(file_content)
    print(file_content)

    process_texts(list)

main()