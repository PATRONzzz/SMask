import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  List,
  ListItem,
  ListItemText,
  Checkbox,
  IconButton,
  TextField,
  Button,
  Paper,
  Grid,
  Accordion,
  AccordionSummary,
  AccordionDetails
} from '@mui/material';
import {
  Add,
  ExpandMore,
  Edit,
  Delete,
  CalendarToday,
  PriorityHigh
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const TaskForm = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [newTask, setNewTask] = useState('');
  const [expanded, setExpanded] = useState(null);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_BASE_URL}/api/tasks`);
        setTasks(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching tasks:', error);
        setLoading(false);
      }
    };
    fetchTasks();
  }, []);
  if (loading) {   
    return <div>Loading...</div>;  } 

  const handleToggle = (taskId) => {
    setTasks(tasks.map(task => 
      task.id === taskId ? {...task, completed: !task.completed} : task
    ));
  };

  const handleAddTask = () => {
    if (newTask.trim()) {
      setTasks([...tasks, {
        id: Date.now(),
        title: newTask,
        completed: false,
        subtasks: []
      }]);
      setNewTask('');
    }
  };

  const handleExpand = (taskId) => {
    setExpanded(expanded === taskId ? null : taskId);
  };

  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            SMask
          </Typography>
          <Button color="inherit">Фильтры</Button>

          <Button 
            color="inherit" 
            component={Link} 
            to="/auth"
            sx={{ mr: 2 }}
          >
            Профиль
          </Button>
        </Toolbar>
      </AppBar>

      <Container maxWidth="md" sx={{ mt: 4 }}>
        <Paper sx={{ p: 2, mb: 2 }}>
          <Grid container spacing={2} alignItems="center">
            <Grid item xs={9}>
              <TextField
                fullWidth
                label="Новая задача"
                variant="outlined"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
              />
            </Grid>
            <Grid item xs={3}>
              <Button
                fullWidth
                variant="contained"
                startIcon={<Add />}
                onClick={handleAddTask}
              >
                Добавить
              </Button>
            </Grid>
          </Grid>
        </Paper>

        <List>
          {tasks.map((task) => (
            <Accordion
              key={task.id}
              expanded={expanded === task.id}
              onChange={() => handleExpand(task.id)}
            >
              <AccordionSummary expandIcon={<ExpandMore />}>
                <Checkbox
                  checked={task.completed}
                  onChange={() => handleToggle(task.id)}
                  color="primary"
                />
                <ListItemText
                  primary={task.title}
                  secondary={
                    <>
                      <PriorityHigh fontSize="small" color={
                        task.priority === 'high' ? 'error' : 
                        task.priority === 'medium' ? 'warning' : 'disabled'
                      } />
                      <CalendarToday fontSize="small" sx={{ ml: 1 }} />
                      <Typography variant="caption" sx={{ ml: 1 }}>
                        {task.dueDate}
                      </Typography>
                    </>
                  }
                />
                <IconButton>
                  <Edit fontSize="small" />
                </IconButton>
                <IconButton>
                  <Delete fontSize="small" />
                </IconButton>
              </AccordionSummary>

              {task.subtasks?.length > 0 && (
                <AccordionDetails>
                  <List sx={{ width: '100%', pl: 4 }}>
                    {task.subtasks.map((subtask) => (
                      <ListItem key={subtask.id}>
                        <Checkbox
                          checked={subtask.completed}
                          onChange={() => handleToggle(subtask.id)}
                          size="small"
                        />
                        <ListItemText
                          primary={subtask.title}
                          secondary={
                            <>
                              <CalendarToday fontSize="small" />
                              <Typography variant="caption" sx={{ ml: 1 }}>
                                {subtask.dueDate}
                              </Typography>
                            </>
                          }
                        />
                        <IconButton size="small">
                          <Edit fontSize="small" />
                        </IconButton>
                        <IconButton size="small">
                          <Delete fontSize="small" />
                        </IconButton>
                      </ListItem>
                    ))}
                  </List>
                </AccordionDetails>
              )}
            </Accordion>
          ))}
        </List>
      
      
      </Container>
    </div>
  );
};

export default TaskForm;