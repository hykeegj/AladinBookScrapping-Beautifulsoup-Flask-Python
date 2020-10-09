from aladin import extract
from save import save_to_file

search_keyword = 'asdf'

books = extract(search_keyword)
print("추출 완료!")

print("csv 파일로 저장중...")
save_to_file(books)
print("저장 완료!!")
