<template>
  <div>
    <div class="auth-container">
      <h2>Login or Register</h2>
      <form>
        <label for="username">Username:</label>
        <input v-model="username" type="text" id="username" required>

        <label for="password">Password:</label>
        <input v-model="password" type="password" id="password" required>
        <!-- Login Button -->
        <button @click.prevent="login" type="button" class="login-btn">Login</button>
        <!-- Register Button -->
        <button @click.prevent="register" type="button" class="register-btn">Register</button>
      </form>
    </div>
  </div>
</template>
  
  <script>
import axios from 'axios';

  export default {
    name: 'LoginView',

    data() {
    return {
      username: '',
      password: '',
    };
  },
    methods: {
      login() {
      // Call the login API using axios
      const apiUrl = 'http://localhost:8000/api/login/';
      const data = { username: this.username, password: this.password };
      axios.post(apiUrl, data)
        .then(response => {
         
          localStorage.setItem('id', response.data.id);
          localStorage.setItem('username', response.data.username);

          console.log('Login successful:', response.data);
          this.$router.push('/');

        })
        .catch(error => {
          window.alert('Login failed. Please check your username and password.');
          console.error('Login error:', error.response.data);
        });
    },
    register() {
      // Call the register API using Axios
      const apiUrl = 'http://localhost:8000/api/register/';
      const data = { username: this.username, password: this.password };

      axios.post(apiUrl, data)
        .then(response => {
          console.log('register successful:', response.data);
          this.username = '';
          this.password = '';
          alert('Registration successful');
        })
        .catch(error => {
          console.error('register error:', error.response.data);
        });
    },
  },
  };
  </script>
  
  
  <style>
  .auth-container {
    max-width: 300px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  label {
    display: block;
    margin-bottom: 8px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    box-sizing: border-box;
  }
  
  button {
    background-color: #4caf50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  .login-btn {
    background-color: #4caf50;
  }
  
  .register-btn {
    background-color: #3498db;
  }
  </style>