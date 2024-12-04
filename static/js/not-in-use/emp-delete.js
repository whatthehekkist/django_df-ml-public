//<script>
        function openDeleteModal(id, name) {
            document.getElementById('deleteId').value = id;
            console.log(document.getElementById('deleteId').value);
            document.getElementById('deleteMessage').innerText = `"${name}"을(를) 삭제하시겠습니까?`;
            document.getElementById('deleteModal').style.display = "block";
        }

        function closeDeleteModal() {
            document.getElementById('deleteModal').style.display = "none";
        }

        function handleDelete(event) {

            console.log("!!!!!!!!!!!!!!!!!!!!!!!!!");
            event.preventDefault();  // 기본 제출 방지
            // 디버깅을 위한 로그
            console.log('formData:', Array.from(formData)); // FormData를 배열로 변환하여 확인
            console.log('deleteId:', formData.get('deleteId')); // deleteId 확인

//            fetch(window.location.href, {
//                method: 'POST',
//                body: formData,
//            })
//            .then(response => {
//                if (response.ok) {
//                    return response.json();
//                }
//                throw new Error('Network response was not ok.');
//            })
//            .then(data => {
//                if (data.status === 'deleted') {
//                    // 삭제 성공 시, 페이지 새로 고침
//                    location.reload();
//                }
//            })
//            .catch(error => console.error('Error:', error));
        }


//    </script>