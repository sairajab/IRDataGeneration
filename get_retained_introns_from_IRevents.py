# Read IR events and introns files
def read_ir_events(file_path):
    ir_events = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            event = {
                "start": int(parts[1]),
                "end": int(parts[2]),
                "gene": parts[3],
                "strand": parts[4],
                "chr": f"chr{parts[5].lower()}"  # Normalize chromosome names
            }
            ir_events.append(event)
    return ir_events

def read_introns(file_path):
    introns = []
    introns_dict = set([])
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            intron = {
                "gene": parts[0],
                "start": int(parts[1]),
                "end": int(parts[2]),
                "strand": parts[3],
                "chr": parts[4].lower()  # Normalize chromosome names
            }
            introns.append(intron)
            introns_dict.add((intron["start"], intron["end"], intron["strand"], intron["chr"]))
    return introns, introns_dict

# Find retained introns
def find_retained_introns(ir_events, introns):
    retained_introns = []
    for intron in introns:
        print(f"Checking intron: {intron}")
        for ir_event in ir_events:
            # Check for same gene, strand, and chromosome, and overlapping coordinates
            if (intron["gene"] == ir_event["gene"] and
                intron["strand"] == ir_event["strand"] and
                intron["chr"] == ir_event["chr"] and
                intron["start"] >= ir_event["start"] and
                intron["end"] <= ir_event["end"]):
                retained_introns.append((intron["gene"], intron["start"], intron["end"], intron["chr"], intron["strand"]))
                break  # No need to check other IR events for this intron
    return retained_introns

# Output retained introns
def write_retained_introns(file_path, retained_introns):
    with open(file_path, 'w') as file:
        for intron in retained_introns:
            line = f"{intron[0]}\t{intron[1]}\t{intron[2]}\t{intron[3]}\t{intron[4]}\n"
            file.write(line)

def find_not_retained_introns(introns, retained_introns):
    not_retained_introns = []
    for intron in introns:
        if intron not in retained_introns:
            not_retained_introns.append(intron)
    return not_retained_introns
# Main function
def main():
    ir_events_file = 'IR_Mus_Musculus_events.txt'  # Replace with your IR events file path
    introns_file = 'all_introns_ensmbl_mus_mus.txt'     # Replace with your introns file path
    #output_file = 'retained_introns_tair10_ensmbl.txt'  # Output file path

    ir_events = read_ir_events(ir_events_file)
    introns, introns_dict = read_introns(introns_file)
    print(f"Read {len(introns)} introns")
    retained_introns = find_retained_introns(ir_events, introns)
    
    #_, retained_introns = read_introns(output_file)
    print(f"Read {len(retained_introns)} retained introns")
    #not_retained_introns = find_not_retained_introns(introns, retained_introns)
    
    output_file = 'retained_introns_ensmble_mus_musculus.txt'
    write_retained_introns(output_file, retained_introns)

    print(f"Retained introns written to {output_file}")

if __name__ == "__main__":
    main()
