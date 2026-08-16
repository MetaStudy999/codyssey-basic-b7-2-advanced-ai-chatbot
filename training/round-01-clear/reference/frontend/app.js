let token = sessionStorage.getItem('access_token') || '';
let currentUser = null;

const $ = (id) => document.getElementById(id);
const errorBox = $('error');

async function api(path, options = {}) {
  const headers = { 'Content-Type': 'application/json', ...(options.headers || {}) };
  if (token) headers.Authorization = `Bearer ${token}`;
  const response = await fetch(path, { ...options, headers });
  if (response.status === 204) return null;
  const body = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(body.detail || `HTTP ${response.status}`);
  return body;
}

function setError(message = '') { errorBox.textContent = message; }

function setAuthUI() {
  const loggedIn = Boolean(currentUser && token);
  $('auth-section').classList.toggle('hidden', loggedIn);
  $('account-section').classList.toggle('hidden', !loggedIn);
  $('chat-section').classList.toggle('hidden', !loggedIn);
  $('post-form').classList.toggle('hidden', !loggedIn);
  $('status').textContent = loggedIn ? '로그인 상태입니다.' : '비로그인 상태입니다.';
  $('me').textContent = loggedIn ? `${currentUser.username} (${currentUser.email})` : '';
}

async function refreshMe() {
  if (!token) { currentUser = null; setAuthUI(); return; }
  try {
    currentUser = await api('/api/auth/me');
  } catch (_) {
    token = '';
    currentUser = null;
    sessionStorage.removeItem('access_token');
  }
  setAuthUI();
}

$('signup-form').addEventListener('submit', async (event) => {
  event.preventDefault(); setError();
  const data = Object.fromEntries(new FormData(event.currentTarget));
  try {
    await api('/api/auth/signup', { method: 'POST', body: JSON.stringify(data) });
    event.currentTarget.reset();
    $('status').textContent = '회원가입 완료. 로그인해 주세요.';
  } catch (error) { setError(error.message); }
});

$('login-form').addEventListener('submit', async (event) => {
  event.preventDefault(); setError();
  const data = Object.fromEntries(new FormData(event.currentTarget));
  try {
    const result = await api('/api/auth/login', { method: 'POST', body: JSON.stringify(data) });
    token = result.access_token;
    sessionStorage.setItem('access_token', token);
    event.currentTarget.reset();
    await refreshMe();
    await loadSessions();
    await loadPosts();
  } catch (error) { setError(error.message); }
});

$('logout-button').addEventListener('click', async () => {
  setError();
  try { await api('/api/auth/logout', { method: 'POST' }); } catch (_) {}
  token = ''; currentUser = null; sessionStorage.removeItem('access_token');
  setAuthUI();
  $('messages').replaceChildren();
  await loadPosts();
});

$('session-form').addEventListener('submit', async (event) => {
  event.preventDefault(); setError();
  const data = Object.fromEntries(new FormData(event.currentTarget));
  try {
    await api('/api/chat/sessions', { method: 'POST', body: JSON.stringify(data) });
    event.currentTarget.reset(); await loadSessions();
  } catch (error) { setError(error.message); }
});

async function loadSessions() {
  if (!token) return;
  try {
    const rows = await api('/api/chat/sessions');
    const select = $('sessions'); select.replaceChildren();
    for (const row of rows) {
      const option = document.createElement('option');
      option.value = row.id; option.textContent = `${row.id}: ${row.title}`;
      select.append(option);
    }
  } catch (error) { setError(error.message); }
}

async function loadMessages() {
  const sessionId = $('sessions').value;
  if (!sessionId) return;
  try {
    const rows = await api(`/api/chat/sessions/${sessionId}/messages`);
    const container = $('messages'); container.replaceChildren();
    for (const row of rows) {
      const div = document.createElement('div'); div.className = 'message';
      const strong = document.createElement('strong'); strong.textContent = `${row.role}: `;
      const text = document.createTextNode(row.content);
      div.append(strong, text); container.append(div);
    }
  } catch (error) { setError(error.message); }
}

$('load-messages').addEventListener('click', loadMessages);

$('message-form').addEventListener('submit', async (event) => {
  event.preventDefault(); setError();
  const sessionId = $('sessions').value;
  if (!sessionId) { setError('먼저 대화 세션을 만들어 주세요.'); return; }
  const data = Object.fromEntries(new FormData(event.currentTarget));
  try {
    await api(`/api/chat/sessions/${sessionId}/messages`, { method: 'POST', body: JSON.stringify(data) });
    event.currentTarget.reset(); await loadMessages();
  } catch (error) { setError(error.message); }
});

$('post-form').addEventListener('submit', async (event) => {
  event.preventDefault(); setError();
  const data = Object.fromEntries(new FormData(event.currentTarget));
  try {
    await api('/api/posts', { method: 'POST', body: JSON.stringify(data) });
    event.currentTarget.reset(); await loadPosts();
  } catch (error) { setError(error.message); }
});

async function editPost(post) {
  const title = window.prompt('제목', post.title);
  if (title === null) return;
  const content = window.prompt('내용', post.content);
  if (content === null) return;
  try {
    await api(`/api/posts/${post.id}`, { method: 'PUT', body: JSON.stringify({ title, content }) });
    await loadPosts();
  } catch (error) { setError(error.message); }
}

async function deletePost(post) {
  if (!window.confirm(`'${post.title}' 글을 삭제할까요?`)) return;
  try { await api(`/api/posts/${post.id}`, { method: 'DELETE' }); await loadPosts(); }
  catch (error) { setError(error.message); }
}

async function loadPosts() {
  try {
    const rows = await api('/api/posts');
    const container = $('posts'); container.replaceChildren();
    for (const post of rows) {
      const div = document.createElement('div'); div.className = 'post';
      const h3 = document.createElement('h3'); h3.textContent = post.title;
      const meta = document.createElement('small'); meta.textContent = `작성자: ${post.author}`;
      const body = document.createElement('p'); body.textContent = post.content;
      div.append(h3, meta, body);
      if (currentUser && post.author_id === currentUser.id) {
        const edit = document.createElement('button'); edit.textContent = '수정'; edit.addEventListener('click', () => editPost(post));
        const remove = document.createElement('button'); remove.textContent = '삭제'; remove.addEventListener('click', () => deletePost(post));
        div.append(edit, remove);
      }
      container.append(div);
    }
  } catch (error) { setError(error.message); }
}

$('reload-posts').addEventListener('click', loadPosts);

(async function boot() {
  await refreshMe();
  if (token) await loadSessions();
  await loadPosts();
})();
