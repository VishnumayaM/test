import dropbox

f=open("data.json")
dbx=dropbox.Dropbox('ibfLCmDojUAAAAAAAAAABhKu4Xz4Tp1CHq3V9NMN0WtNRfKw1KqPphVhnxdMslCr')
dbx.files_upload(f,"/uploaded.json")
f.close()
