# B7-2 Collaboration Runtime Template

공식 요구는 **실제 Git 이력**으로 검증합니다. Reference 문서만으로 PASS하지 않습니다.

## Branch strategy

```text
feature/<name> → develop → main
```

- `main` 직접 push 금지
- 기능 단위 feature branch
- Pull Request로 develop 병합
- 최종 develop → main도 Pull Request

## 팀 역할

Phase C에서 실제 팀원 정보로 채웁니다.

| 팀원 | 역할 | 담당 기능 | 주요 PR | 유의미 커밋 수 |
|---|---|---|---|---:|
| NEEDS-RUNTIME |  |  |  | 0 |

각 팀원은 공식 요구대로 **10회 이상의 유의미한 커밋**을 실제로 만들어야 합니다.

## 유의미한 커밋 예

- auth signup/login 기능
- chat ownership 검사
- message persistence
- post CRUD/owner policy
- frontend auth UI
- API spec/ERD/architecture 실제 변경

단순 공백/문구만 반복 변경해 횟수를 채우지 않습니다.
