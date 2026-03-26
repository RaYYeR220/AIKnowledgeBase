-- Mock schema for a simple hybrid retrieval system

create table if not exists notes (
  id integer primary key,
  path text unique not null,
  note_type text,
  title text,
  metadata_json text,
  content text not null,
  content_hash text,
  status text default 'active',
  created_at text,
  updated_at text
);

create table if not exists chunks (
  id integer primary key,
  note_id integer not null references notes(id) on delete cascade,
  chunk_index integer not null,
  chunk_text text not null,
  token_count integer,
  embedding_ref text,
  unique(note_id, chunk_index)
);

create virtual table if not exists chunks_fts using fts5(
  path,
  title,
  chunk_text,
  content=''
);

create table if not exists reindex_queue (
  id integer primary key,
  path text not null,
  reason text,
  queued_at text,
  processed_at text,
  status text default 'queued'
);
