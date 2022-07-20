from cs_3308.bag_of_words_assignment.indexer import Indexer

indexer = Indexer()
stop_dict = indexer.read_stop_dict()
indexer.bag_of_words()
indexer.scan_directroy()
indexer.write_to_file()
indexer.get_unique_terms()
indexer.write_index_to_disk()
indexer.term_frequency()
indexer.output_print()
