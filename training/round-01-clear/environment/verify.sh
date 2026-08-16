#!/usr/bin/env bash
set -u

ROUND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF_DIR="$ROUND_DIR/reference"
PASS=0
FAIL=0
pass(){ printf '[PASS] %s\n' "$1"; PASS=$((PASS+1)); }
fail(){ printf '[FAIL] %s\n' "$1"; FAIL=$((FAIL+1)); }

for path in \
  "$REF_DIR/requirements.txt" \
  "$REF_DIR/.env.example" \
  "$REF_DIR/backend/main.py" \
  "$REF_DIR/backend/models.py" \
  "$REF_DIR/backend/security.py" \
  "$REF_DIR/backend/dependencies.py" \
  "$REF_DIR/backend/ai_client.py" \
  "$REF_DIR/backend/routers/auth.py" \
  "$REF_DIR/backend/routers/chat.py" \
  "$REF_DIR/backend/routers/posts.py" \
  "$REF_DIR/frontend/index.html" \
  "$REF_DIR/frontend/app.js"
do
  [[ -f "$path" ]] && pass "file exists: ${path#$ROUND_DIR/}" || fail "missing: ${path#$ROUND_DIR/}"
done

if command -v python3 >/dev/null 2>&1 && python3 -m compileall -q "$REF_DIR/backend"; then
  pass "Python syntax compileall"
else
  fail "Python syntax compileall"
fi

if command -v node >/dev/null 2>&1; then
  node --check "$REF_DIR/frontend/app.js" >/dev/null 2>&1 && pass "JavaScript syntax" || fail "JavaScript syntax"
else
  printf '[INFO] node not installed; JavaScript syntax check deferred\n'
fi

MODELS="$REF_DIR/backend/models.py"
[[ "$(grep -c '^class ' "$MODELS")" -ge 5 ]] && pass "five core ORM entities" || fail "five core ORM entities"

grep -q 'hash_password' "$REF_DIR/backend/routers/auth.py" && pass "signup stores hashed password" || fail "signup stores hashed password"
grep -q 'new_access_token' "$REF_DIR/backend/routers/auth.py" && pass "login issues access token" || fail "login issues access token"
grep -q 'ChatSession.user_id == user_id' "$REF_DIR/backend/routers/chat.py" && pass "chat ownership check" || fail "chat ownership check"
grep -q 'post.user_id != user_id' "$REF_DIR/backend/routers/posts.py" && pass "post ownership check" || fail "post ownership check"
grep -q 'AI_API_KEY' "$REF_DIR/backend/ai_client.py" && pass "AI key comes from environment" || fail "AI key comes from environment"

if grep -R -nE '(sk-[A-Za-z0-9_-]{20,}|BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY)' "$REF_DIR" --exclude='.env.example' >/dev/null 2>&1; then
  fail "no obvious committed credential patterns"
else
  pass "no obvious committed credential patterns"
fi

printf 'Result: %d PASS / %d FAIL\n' "$PASS" "$FAIL"
[[ "$FAIL" -eq 0 ]]
