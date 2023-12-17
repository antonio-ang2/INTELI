import React, { useState } from 'react';
import axios from 'axios';

const CreateNote = () => {
  const [note, setNote] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/grades', { grade: note, user_id: 1 }); // Substitua 1 pelo ID do usuário logado
      console.log('Note created:', response.data.message);
      setNote(''); // Limpa o campo de nota após criar
    } catch (error) {
      console.error('Error creating note:', error);
    }
  };

  return (
    <div>
      <h2>Create Note</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Note:</label>
          <textarea
            value={note}
            onChange={(e) => setNote(e.target.value)}
          />
        </div>
        <button type="submit">Save Note</button>
      </form>
    </div>
  );
};

export default CreateNote;
