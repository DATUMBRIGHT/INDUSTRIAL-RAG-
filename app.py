import time
import uuid
from pathlib import Path

import streamlit as st

# ── Page config (must be first Streamlit call) ────────────────────────────────
st.set_page_config(
    page_title="Industrial RAG",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
/* ── Global ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp { background: #0d0f14; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #131720;
    border-right: 1px solid #1e2433;
}
[data-testid="stSidebar"] * { color: #c9d1e0 !important; }

/* ── Header badge ── */
.header-wrap {
    display: flex; align-items: center; gap: 12px;
    padding: 1.2rem 0 0.4rem 0;
}
.header-icon {
    font-size: 2rem;
    background: linear-gradient(135deg, #f97316, #fb923c);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.header-title {
    font-size: 1.55rem; font-weight: 700;
    background: linear-gradient(90deg, #f97316 0%, #facc15 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1.1;
}
.header-sub { font-size: 0.78rem; color: #64748b; margin-top: 2px; }

/* ── Status pill ── */
.pill {
    display: inline-block; padding: 3px 10px;
    border-radius: 20px; font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.04em;
}
.pill-green  { background: #14532d55; color: #4ade80; border: 1px solid #166534; }
.pill-yellow { background: #78350f55; color: #fbbf24; border: 1px solid #92400e; }
.pill-red    { background: #7f1d1d55; color: #f87171; border: 1px solid #991b1b; }

/* ── Chat container ── */
.chat-area {
    max-width: 860px; margin: 0 auto;
    padding-bottom: 120px;
}

/* ── Message bubbles ── */
.msg-row { display: flex; gap: 12px; margin-bottom: 1.4rem; align-items: flex-start; }
.msg-row.user  { flex-direction: row-reverse; }

.avatar {
    width: 36px; height: 36px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; flex-shrink: 0;
}
.avatar-user { background: linear-gradient(135deg, #f97316, #fb923c); }
.avatar-bot  { background: linear-gradient(135deg, #1e40af, #3b82f6); }

.bubble {
    max-width: 78%; padding: 0.85rem 1.1rem;
    border-radius: 16px; line-height: 1.65;
    font-size: 0.92rem; color: #e2e8f0;
}
.bubble-user {
    background: linear-gradient(135deg, #1c2a4a, #1e3a5f);
    border: 1px solid #2563eb44;
    border-top-right-radius: 4px;
}
.bubble-bot {
    background: #161b27;
    border: 1px solid #1e2433;
    border-top-left-radius: 4px;
}

/* ── Meta line under bot bubble ── */
.meta { font-size: 0.7rem; color: #475569; margin-top: 6px; }

/* ── Source cards ── */
.sources-wrap { margin-top: 10px; display: flex; flex-wrap: wrap; gap: 6px; }
.source-chip {
    background: #0f172a; border: 1px solid #1e2d4a;
    border-radius: 8px; padding: 4px 10px;
    font-size: 0.7rem; color: #7dd3fc;
    cursor: default;
}

/* ── Welcome card ── */
.welcome-card {
    background: #131720; border: 1px solid #1e2433;
    border-radius: 16px; padding: 2rem 2.4rem;
    max-width: 600px; margin: 3rem auto 0;
    text-align: center;
}
.welcome-card h2 { color: #f8fafc; margin-bottom: 0.5rem; }
.welcome-card p  { color: #64748b; font-size: 0.88rem; line-height: 1.6; }
.example-queries { margin-top: 1.4rem; display: flex; flex-direction: column; gap: 8px; }
.example-q {
    background: #0d0f14; border: 1px solid #1e2433;
    border-radius: 10px; padding: 0.6rem 1rem;
    color: #94a3b8; font-size: 0.82rem;
    text-align: left; cursor: pointer;
}

/* ── Divider ── */
hr.divider { border: none; border-top: 1px solid #1e2433; margin: 1rem 0; }

/* ── Spinner override ── */
.stSpinner > div { border-top-color: #f97316 !important; }
</style>
""",
    unsafe_allow_html=True,
)

# ── Lazy imports (avoid slow imports on every rerun) ──────────────────────────
@st.cache_resource(show_spinner=False)
def load_engine():
    from RAG.chunker import DocChunker
    from RAG.queryengine import RAGQueryEngine
    from logger.rag_logger import QueryLogger

    t0 = time.perf_counter()
    processed_docs_path = Path(__file__).parent / "processed_docs"
    chunker = DocChunker(folder_path=processed_docs_path)
    index = chunker.run()
    elapsed = (time.perf_counter() - t0) * 1000

    qlog = QueryLogger()
    storage_source = "disk" if (Path(__file__).parent / "storage").exists() else "fresh embed"
    qlog.log_index_load(elapsed, storage_source)

    engine = RAGQueryEngine(index=index)
    return engine, qlog


# ── Session state ─────────────────────────────────────────────────────────────
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]
if "messages" not in st.session_state:
    st.session_state.messages = []
if "engine_ready" not in st.session_state:
    st.session_state.engine_ready = False
if "engine_error" not in st.session_state:
    st.session_state.engine_error = None


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Industrial RAG")
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Index status
    st.markdown("**Index**")
    if st.session_state.engine_error:
        st.markdown('<span class="pill pill-red">● Error</span>', unsafe_allow_html=True)
        st.caption(str(st.session_state.engine_error)[:120])
    elif st.session_state.engine_ready:
        st.markdown('<span class="pill pill-green">● Ready</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="pill pill-yellow">● Loading…</span>', unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Model info
    st.markdown("**Model**")
    st.caption("qwen3.5:35b-a3b via Ollama")
    st.markdown("**Embeddings**")
    st.caption("nomic-embed-text-v1.5 (FastEmbed)")
    st.markdown("**Retrieval**")
    st.caption("BM25 + Vector fusion → cross-encoder rerank")

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Session info
    st.markdown("**Session**")
    st.caption(f"`{st.session_state.session_id}`")
    msg_count = len(st.session_state.messages)
    st.caption(f"{msg_count // 2} exchanges")

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    if st.button("🗑 Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("**Logs**")
    log_dir = Path(__file__).parent / "logger" / "logs"
    if log_dir.exists():
        log_files = sorted(log_dir.glob("*.log"), reverse=True)[:3]
        for lf in log_files:
            st.caption(f"📄 {lf.name}")
    else:
        st.caption("No logs yet")


# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="header-wrap">
        <span class="header-icon">⚙️</span>
        <div>
            <div class="header-title">Industrial RAG Assistant</div>
            <div class="header-sub">Allen-Bradley · Rockwell Automation · PLC & Drive Manuals</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Load engine once ──────────────────────────────────────────────────────────
if not st.session_state.engine_ready and not st.session_state.engine_error:
    with st.spinner("Loading index and initialising models…"):
        try:
            engine, qlog = load_engine()
            st.session_state.engine_ready = True
            st.rerun()
        except Exception as e:
            st.session_state.engine_error = e
            st.rerun()
else:
    if st.session_state.engine_ready:
        engine, qlog = load_engine()


# ── Render chat history ───────────────────────────────────────────────────────
def render_message(role: str, content: str, meta: str = "", sources: list = None):
    if role == "user":
        st.markdown(
            f"""
            <div class="msg-row user">
                <div class="avatar avatar-user">👤</div>
                <div class="bubble bubble-user">{content}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        source_html = ""
        if sources:
            chips = "".join(
                f'<span class="source-chip" title="{s.get("file", "")}">'
                f'📄 {s.get("file", "source")}</span>'
                for s in sources
            )
            source_html = f'<div class="sources-wrap">{chips}</div>'

        st.markdown(
            f"""
            <div class="msg-row">
                <div class="avatar avatar-bot">🤖</div>
                <div>
                    <div class="bubble bubble-bot">{content}</div>
                    {source_html}
                    <div class="meta">{meta}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown('<div class="chat-area">', unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown(
        """
        <div class="welcome-card">
            <h2>What can I help you with?</h2>
            <p>Ask anything about Allen-Bradley PLCs, drives, I/O modules,
            safety systems, or Rockwell Automation manuals.</p>
            <div class="example-queries">
                <div class="example-q">How do I replace a 1756-UM001-EN-P module in a ControlLogix system?</div>
                <div class="example-q">What are the PowerFlex 750 fault codes and how do I clear them?</div>
                <div class="example-q">How do I configure EtherNet/IP on a CompactLogix controller?</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    for msg in st.session_state.messages:
        render_message(
            role=msg["role"],
            content=msg["content"],
            meta=msg.get("meta", ""),
            sources=msg.get("sources", []),
        )

st.markdown("</div>", unsafe_allow_html=True)

# ── Chat input ────────────────────────────────────────────────────────────────
if prompt := st.chat_input(
    "Ask about PLCs, drives, I/O modules…",
    disabled=not st.session_state.engine_ready,
):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Query engine
    with st.spinner("Thinking…"):
        try:
            t0 = time.perf_counter()
            response = engine.query(prompt)
            latency_ms = (time.perf_counter() - t0) * 1000

            # Extract source file names from response nodes
            sources = []
            if hasattr(response, "source_nodes"):
                seen = set()
                for node in response.source_nodes:
                    fname = node.metadata.get("file_name", "")
                    if fname and fname not in seen:
                        seen.add(fname)
                        sources.append({"file": fname, "score": round(node.score or 0, 3)})

            response_text = str(response)
            meta = f"⏱ {round(latency_ms)}ms · {len(sources)} sources · session {st.session_state.session_id}"

            # Log it
            qlog.log_query(
                query=prompt,
                response=response_text,
                sources=sources,
                latency_ms=latency_ms,
                session_id=st.session_state.session_id,
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response_text,
                    "meta": meta,
                    "sources": sources,
                }
            )

        except Exception as e:
            from logger.rag_logger import QueryLogger
            QueryLogger().log_error("query", e)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": f"⚠️ Error: {e}",
                    "meta": "",
                    "sources": [],
                }
            )

    st.rerun()
