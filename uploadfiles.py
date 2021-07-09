import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from,file_to):
        dbx = dropbox.Dropbox(self,access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

    def main():
        access_token = 'sl.A0TWqd_wyWPY9ZJxHS5Y8KdcjStTfjCflWhqn6dTE4qVYg5clNL0YWMyl73kvGCu03VD2-n7kjiN0DoI2jqcFD7_9GOMswmJi24Lxp4QkMmJ3swAxaA0Os3yF-EahBfpBNTwF0A'
        transferData = TransferData(access_token)

        file_from = input("Enter the file path to transfer:-")
        file_to = input("Enter the full path to upload to dropbox:-")

        transferData.upload_file(file_from , file_to)
        print("file has been moved successfully!!!!")