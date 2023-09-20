# 2주차 파이썬

## 목차
1. 파이썬 기본 구조
2. 클래스와 상속
3. 로깅과 쓰레드 기반 콜백 구현

### 2-1 파이썬 기본구조 수업내용
- vscode로 들어온 이후에 remote wsl로 접속
- c/VScode/bin/code 시작
- remote WSL 선택하기
- open folder -> Project_ROS
- 패키지 추가 해야함
- vscode에서 터미널을 열어서 아래 명령어 입력
- $ sudo pip3 install numpy matplotlib pandas scipy
- 기본적으로 파이썬에서 필수로 거의 사용되는 패키지
- wsl에서 GUI로 결과를 보여주기 위해서 https://psychoria.tistory.com/739 여기 페이지 참고
- 간략하게 설명하면 VcXsrv Window X server 설치함
- 이후 wsl에서 sudo nano ~/.bashrc 들어간다음 맨 마지막 줄에
- export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"
- export LIBGL_ALWAYS_INDIRECT=1
- 위 두줄의 코드를 작성해줍니다.
- 그리고 $ sudo apt install -y gedit firefox
- 이 명령어를 통해 실행하면 바로 진행됩니다.


