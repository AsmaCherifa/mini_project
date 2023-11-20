<template>    
<NavbarVue></NavbarVue>
  <div class="dashboard-container">
    <h1 class="display-2">List of Audios</h1>


    <div v-if="username" class="welcome-message">
      <p>Welcome, {{ username }}</p>
      <button @click.prevent="logout" type="button" class="login-btn">Logout</button>

    </div>

    <table class="audio-table">
      <thead>
        <tr>
          <th>Record Name</th>
          <th>Audio</th>
          <th>Status</th>
          <th>Transcription</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="audio in audioSegments" :key="audio.id">
          <td>{{ audio.record_name }}</td>
          <td>
            <audio controls>
              <source :src="'http://localhost:8000/api' + audio.audio_file" type="audio/mp3">
            </audio>
          </td>
          <td :class="{'submitted-status': audio.status === 'submitted', 'available-status': audio.status !== 'submitted'}">
            {{ audio.status }}
          </td>
          <td v-if="audio.status !== 'submitted'">
            <textarea v-model="localTranscriptionText"></textarea>
          </td>
          <td>
            <button v-if="audio.status === 'available'" @click.prevent="transcribeAudio(audio)" class="transcribe-btn">
              Transcribe
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios';
import NavbarVue from '@/components/NavbarVue.vue';

export default {
  name: 'HomeView',
    components: {
      NavbarVue
  },
    data() {
        return {
            audioSegments: [],
            username: '',
        };
    },
    
    mounted() {
        this.fetchAudioSegments();
        this.username = localStorage.getItem('username');

    },

    methods: {
        async fetchAudioSegments() {
            try {
                const response = await axios.get('http://localhost:8000/api/audio/');
                this.audioSegments = response.data;
            } catch (error) {
                console.error('Error fetching audio segments:', error);
            }
        },
        logout() {
          // Clear  localStorage
          localStorage.removeItem('id');
          localStorage.removeItem('username');
          this.$router.push('/login');
        },
        async transcribeAudio(audio) {
         
        try {

            const userId = localStorage.getItem('id');
            const response = await axios.post('http://localhost:8000/api/transcription/', {
              text: this.localTranscriptionText,
                annotator: userId,  
                audio_id: audio.id,
            });
            alert('Transcription successful');
            window.location.reload();

            console.log('Transcription added successfully:', response.data);
        } catch (error) {
            console.error('Error adding transcription:', error);
            alert('Invalid characters in transcription text. Please correct it.');

        }
    },

    },
};
</script>

<style>
.dashboard-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.welcome-message {
  margin-top: 20px;
}

.audio-table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
}
.submitted-status {
  color: red;
}

.available-status {
  color: green;
}
.audio-table th, .audio-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.transcribe-btn {
  background-color: #3498db;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.transcribe-btn:hover {
  background-color: #2980b9;
}
</style>
