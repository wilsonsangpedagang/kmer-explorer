repeat = True
while repeat == True:
    # reverse complementary strand
    try:
        genome_file = input("Genome file name: ")  # input genome file name
        print(""" Choose an option:
            [1] Compute a reverse complement of a k-mer pattern
            [2] Count a k-mer pattern
            [3] Find most frequent k-mer patterns """)

        select_operation = input("Select an operation [1/2/3]: ")  # select which Operation you want to choose

        genome = open(genome_file, "r").read()  # To read a txt file and convert it into a string


        def reverse_pattern(pattern):
            complementary_pattern = ""  # for storing the result of the reversing operation

            for each_character in pattern:
                temp = each_character  # temporary variable just to keep the each_character original in case of multiple usage
                if temp == "A":
                    complementary_pattern += "T"  # to convert the original genome to its complement
                if temp == "C":
                    complementary_pattern += "G"
                if temp == "G":
                    complementary_pattern += "C"
                if temp == "T":
                    complementary_pattern += "A"
            complementary_pattern = complementary_pattern[:: -1]  # to read the string backward so it will become the genome complement
            return complementary_pattern


        def count_k_mer(genome, pattern):
            complement_pattern = reverse_pattern(pattern)  # to convert pattern into its complement
            occurence = 0  # to store the occurences of a genome
            for i in range(len(genome) - len(pattern) + 1):
                k_mer = genome[i:i + len(
                    pattern)]  # to slice the string from the index of the pattern until the length of the pattern
                if k_mer == pattern:  # to identify whether the k_mer is its orignal pattern or its complement
                    occurence += 1
                elif k_mer == complement_pattern:
                    occurence += 1
            return occurence  # to return the value of occurence


        def frequent_k_mer(genome, k):  # k is the number of char of the mer
            mers = []  # to store all of the original or complement mer
            same_occurence = []  # to store all of the mers that have the same occurence
            original_mers = []  # to store only the original mers
            max_count = 0  # the initial count of the mers
            frequent_mer = None  # the most frequent mer
            for i in range(len(genome) - int(k) + 1):
                k_mer = genome[i:i + int(k)]
                mers.append(k_mer)  # to append all of the sliced mer into mers
                original_mers.append(k_mer)  # to append all of the original mer
                complement = reverse_pattern(k_mer)  # the complement of the k_mer
                mers.append(str(complement))  # append the complement into mers
            for each_mer in mers:
                count_each_mer = count_k_mer(genome, each_mer)  # to count the occurences of each mer
                if count_each_mer > max_count:  # to compare each mer occurence. if the second mer occurence is bigger than the first one, the max count become the occurence of the second one
                    max_count = count_each_mer
                    same_occurence = [each_mer]  # to reset the mer that has the highest occurence into a new one
                elif max_count == count_each_mer:  # appending two or more mer into the same_occurence if both of the occurence are the same
                    same_occurence.append(each_mer)
            filter_complement = []  # to store only the original mers because in the same_occurence, both of them are appended
            for each in same_occurence:
                if each in original_mers:
                    filter_complement.append(each)

            frequent_mer = set(filter_complement)  # eventhough filter_complement contains all of the original mer that has the highest occurence, the element of the list is still duplicated based to its occurence
            # we are making frequent mer into a set and because a set cannot have duplicated element, it only returns the most frequent mer
            return frequent_mer


        if select_operation == "1":
            pattern = input("Input your value of k : ")
            print(reverse_pattern(pattern))
            break

        elif select_operation == "2":
            pattern = input("Input your value of k : ")
            print(count_k_mer(genome, pattern))
            break

        elif select_operation == "3":
            k = input("Input your value of k : ")
            print(frequent_k_mer(genome, k))
            break


    except:
        print("File not found ! ")
        repeat = True
















