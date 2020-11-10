import keyboard
import time
import github_contents

a=str(input("Enter Username:"))

score=0

github = github_contents.GithubContents(
"AlphaBlaze051",
"Competition",#Repository name
'868613781428360c13618d4051d01e5b8c9abad2')

print('ready')
keyboard.wait(' ')
while keyboard.is_pressed(' '):
    time.sleep(1)
    score+=1

c=str(str(a)+'s'+' '+'finale score:'+str(score)+' seconds')
c=c.encode()
print(c)

content_sha, commit_sha = github.write(
    filepath=str(a+'.txt'),#file name
    content_bytes=c,#message to left behind
    commit_message="updated by "+a,
    committer={
        "name": 'AlphaBlaze051',
        "email": 'User',
    },
)