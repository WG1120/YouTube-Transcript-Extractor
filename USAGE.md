# 사용법

## 1. 가상환경 활성화

```bash
cd C:\Users\wnsdn\v_code\009_extracting_yt_scripts
venv\Scripts\activate
```

## 2. 프로그램 실행

```bash
python youtube_transcript_extractor.py
```

## 3. URL 입력

프롬프트가 나타나면 유튜브 URL을 붙여넣기합니다:

```
유튜브 URL을 입력하세요: https://www.youtube.com/watch?v=영상ID
```

## 4. 결과 확인

- **화면**: 자막 전체가 터미널에 출력됩니다.
- **파일**: 같은 디렉토리에 `transcript_영상ID.txt` 파일이 자동 저장됩니다.

## 지원하는 URL 형식

| 형식 | 예시 |
|------|------|
| 일반 | `https://www.youtube.com/watch?v=UF8uR6Z6KLc` |
| 단축 | `https://youtu.be/UF8uR6Z6KLc` |
| Shorts | `https://www.youtube.com/shorts/영상ID` |
| 임베드 | `https://www.youtube.com/embed/영상ID` |

## 참고

- 자막 우선순위: 한국어 → 영어 → 기타 사용 가능한 자막
- 자막이 아예 없는 영상은 안내 메시지가 출력됩니다.
