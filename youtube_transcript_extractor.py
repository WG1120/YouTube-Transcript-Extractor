"""YouTube Transcript Extractor

유튜브 URL을 입력하면 해당 영상의 자막(스크립트)을 추출하여
화면에 출력하고 .txt 파일로 저장하는 프로그램입니다.
"""

import re
import sys
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str) -> str | None:
    """유튜브 URL에서 동영상 ID를 추출합니다."""
    patterns = [
        r"(?:v=|\/v\/|youtu\.be\/)([a-zA-Z0-9_-]{11})",
        r"(?:embed\/)([a-zA-Z0-9_-]{11})",
        r"(?:shorts\/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_transcript(video_id: str) -> str:
    """동영상 ID를 받아 자막 텍스트를 반환합니다.

    한국어 자막을 우선 시도하고, 없으면 영어, 그래도 없으면
    사용 가능한 첫 번째 자막을 가져옵니다.
    """
    ytt_api = YouTubeTranscriptApi()
    try:
        transcript = ytt_api.fetch(video_id, languages=["ko", "en"])
    except Exception:
        # 지정 언어가 없으면 사용 가능한 첫 번째 자막 시도
        transcript_list = ytt_api.list(video_id)
        first_transcript = next(iter(transcript_list))
        transcript = first_transcript.fetch()

    return "\n".join(snippet.text for snippet in transcript)


def save_to_file(text: str, video_id: str) -> str:
    """자막 텍스트를 .txt 파일로 저장하고 파일명을 반환합니다."""
    filename = f"transcript_{video_id}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename


def main():
    """메인 실행 함수"""
    url = input("유튜브 URL을 입력하세요: ").strip()

    if not url:
        print("URL이 입력되지 않았습니다.")
        sys.exit(1)

    video_id = extract_video_id(url)
    if not video_id:
        print("올바른 유튜브 URL이 아닙니다. 다시 확인해주세요.")
        sys.exit(1)

    print(f"\n동영상 ID: {video_id}")
    print("자막을 가져오는 중...\n")

    try:
        transcript_text = get_transcript(video_id)
    except Exception as e:
        print(f"자막을 가져올 수 없습니다: {e}")
        print("이 영상에는 자막(자동 생성 포함)이 제공되지 않을 수 있습니다.")
        sys.exit(1)

    # 화면 출력
    print("=" * 60)
    print("  추출된 자막 (Transcript)")
    print("=" * 60)
    print(transcript_text)
    print("=" * 60)

    # 파일 저장
    filename = save_to_file(transcript_text, video_id)
    print(f"\n자막이 '{filename}' 파일로 저장되었습니다.")


if __name__ == "__main__":
    main()
