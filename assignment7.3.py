def parse_mbox(file_name):
    with open(file_name, 'r') as file:
        senders = []
        for line in file:
            if line.startswith('From '):
                sender = line.split()[1]
                senders.append(sender)
        return senders

def main():
    senders = parse_mbox('mbox.txt')
    for sender in senders:
        print(sender)
    print('Number of senders found:', len(senders))

if __name__ == '__main__':
    main()