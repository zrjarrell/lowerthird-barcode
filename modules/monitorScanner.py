from modules.makeBarcodes import getFullName

def monitorScanner(scanner, queue):
    while True:
        reading = scanner.read(14).decode('utf-8')
        #print(reading)
        scanner.reset_input_buffer()
        queue.enqueue(reading[0:11])


# def monitorScanner(scanner):
#     try:
#         while True:
#             reading = scanner.read(13).decode('utf-8')
#             print(reading)
#             scanner.reset_input_buffer()
#             with open('queue.txt', 'a') as queue:
#                 queue.write(reading)
#     except KeyboardInterrupt:
#         pass



# def monitorScanner(scanner):
#     try:
#         while True:
#             reading = scanner.read(13).decode('utf-8')
#             scanner.reset_input_buffer()
#             if reading[-1] == '>':
#                 with open('queue.txt', 'a') as queue:
#                     queue.write(reading)
#     except KeyboardInterrupt:
#         pass




