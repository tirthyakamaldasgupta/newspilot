import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

interface Message {
  role: 'user' | 'assistant';
  roleIcon: 'bi-robot' | 'bi-person-circle';
  alertClass: 'alert-light' | 'alert-primary';
  alertAlignmentClass: 'justify-content-start' | 'justify-content-end'
  message: string;
}

@Component({
  selector: 'app-index',
  imports: [CommonModule],
  templateUrl: './index.component.html',
  styleUrl: './index.component.css',
})
export class IndexComponent {
  messages: Message[] = [
    {
      role: 'assistant',
      roleIcon: 'bi-robot',
      alertClass: 'alert-light',
      alertAlignmentClass: 'justify-content-start',
      message: 'How can I assist you today?',
    },
    {
      role: 'user',
      roleIcon: 'bi-person-circle',
      alertClass: 'alert-primary',
      alertAlignmentClass: 'justify-content-end',
      message: 'Hello, how are you?',
    },
  ];
}
