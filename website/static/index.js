function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/tasks";
  });
}


function deletebookmark(bookId) {
  console.log('--------------')
  fetch("/delete-bookmark", {
    method: "POST",
    body: JSON.stringify({ bookId: bookId }),
  }).then((_res) => {
    window.location.href = "/bookmarks";
  });
}


function deletePost(postId) {
  fetch("/delete-post", {
    method: "POST",
    body: JSON.stringify({ postId: postId }),
  }).then((_res) => {
    window.location.href = "/myposts";
  });
}


function deleteComp(compId) {
  fetch("/delete-competition", {
    method: "POST",
    body: JSON.stringify({ compId: compId }),
  }).then((_res) => {
    window.location.href = "/competition";
  });
}

function deleteJob(jobId) {
  fetch("/delete-jobintern", {
    method: "POST",
    body: JSON.stringify({ jobId: jobId }),
  }).then((_res) => {
    window.location.href = "/jobs";
  });
}
