-- Enable UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Family groups
CREATE TABLE family_groups (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  active BOOLEAN DEFAULT TRUE
);

-- Group members
CREATE TABLE group_members (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  profile VARCHAR(20) CHECK (profile IN ('administrador','integrante')) DEFAULT 'integrante',
  joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(group_id, user_id)
);

-- Categories
CREATE TABLE categories (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  name VARCHAR(100) NOT NULL,
  type VARCHAR(10) CHECK (type IN ('receita','despesa')) NOT NULL,
  icon VARCHAR(50),
  is_default BOOLEAN DEFAULT FALSE,
  active BOOLEAN DEFAULT TRUE
);

-- Accounts
CREATE TABLE accounts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  name VARCHAR(100) NOT NULL,
  owner_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
  type VARCHAR(20) CHECK (type IN ('corrente','poupanca','investimento','carteira','conjunta')) NOT NULL,
  initial_balance NUMERIC(15,2) DEFAULT 0,
  current_balance NUMERIC(15,2) DEFAULT 0,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Incomes
CREATE TABLE incomes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  account_id UUID REFERENCES accounts(id) ON DELETE SET NULL,
  category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
  description VARCHAR(150) NOT NULL,
  amount NUMERIC(15,2) NOT NULL CHECK (amount > 0),
  receipt_date DATE,
  due_date DATE,
  type VARCHAR(20) DEFAULT 'variavel',
  status VARCHAR(15) CHECK (status IN ('prevista','recebida')) DEFAULT 'prevista',
  recurring BOOLEAN DEFAULT FALSE,
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Expenses
CREATE TABLE expenses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  payer_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
  account_id UUID REFERENCES accounts(id) ON DELETE SET NULL,
  category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
  description VARCHAR(150) NOT NULL,
  total_amount NUMERIC(15,2) NOT NULL CHECK (total_amount > 0),
  purchase_date DATE,
  due_date DATE,
  payment_date DATE,
  expense_type VARCHAR(15) CHECK (expense_type IN ('fixa','variavel','eventual')) DEFAULT 'variavel',
  payment_method VARCHAR(15) CHECK (payment_method IN ('dinheiro','pix','debito','credito','transferencia','outro')) DEFAULT 'dinheiro',
  status VARCHAR(15) CHECK (status IN ('pendente','paga','vencida','cancelada')) DEFAULT 'pendente',
  responsibility VARCHAR(15) CHECK (responsibility IN ('rita','jean','compartilhada')) DEFAULT 'compartilhada',
  private BOOLEAN DEFAULT FALSE,
  notes TEXT,
  receipt_path TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Expense splits
CREATE TABLE expense_splits (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  expense_id UUID REFERENCES expenses(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  amount_due NUMERIC(15,2) NOT NULL,
  percentage NUMERIC(5,2),
  paid BOOLEAN DEFAULT FALSE,
  amount_paid_by_user NUMERIC(15,2) DEFAULT 0,
  note VARCHAR(150),
  UNIQUE(expense_id, user_id)
);

-- Invoices
CREATE TABLE invoices (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  card_id UUID REFERENCES credit_cards(id) ON DELETE CASCADE,
  reference_month INTEGER NOT NULL CHECK (reference_month BETWEEN 1 AND 12),
  reference_year INTEGER NOT NULL,
  closing_date DATE,
  due_date DATE,
  total_amount NUMERIC(15,2) NOT NULL DEFAULT 0,
  paid_amount NUMERIC(15,2) NOT NULL DEFAULT 0,
  status VARCHAR(15) CHECK (status IN ('aberta','fechada','paga','vencida')) DEFAULT 'aberta',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Credit cards
CREATE TABLE credit_cards (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  name VARCHAR(100) NOT NULL,
  institution VARCHAR(100),
  total_limit NUMERIC(15,2) NOT NULL DEFAULT 0,
  available_limit NUMERIC(15,2) NOT NULL DEFAULT 0,
  closing_day INTEGER NOT NULL CHECK (closing_day BETWEEN 1 AND 31),
  due_day INTEGER NOT NULL CHECK (due_day BETWEEN 1 AND 31),
  payment_account_id UUID REFERENCES accounts(id) ON DELETE SET NULL,
  status VARCHAR(15) CHECK (status IN ('ativo','bloqueado','cancelado')) DEFAULT 'ativo',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Card purchases
CREATE TABLE card_purchases (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  card_id UUID REFERENCES credit_cards(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  description VARCHAR(150) NOT NULL,
  total_amount NUMERIC(15,2) NOT NULL,
  installments INTEGER NOT NULL DEFAULT 1 CHECK (installments >= 1),
  installment_value NUMERIC(15,2) NOT NULL,
  purchase_date DATE NOT NULL,
  category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
  responsibility VARCHAR(15) CHECK (responsibility IN ('rita','jean','compartilhada')) DEFAULT 'compartilhada',
  note TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Card installments
CREATE TABLE card_installments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  card_id UUID REFERENCES credit_cards(id) ON DELETE CASCADE,
  purchase_id UUID REFERENCES card_purchases(id) ON DELETE CASCADE,
  invoice_id UUID REFERENCES invoices(id) ON DELETE SET NULL,
  user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,
  installment_number INTEGER NOT NULL,
  installment_value NUMERIC(15,2) NOT NULL,
  due_date DATE NOT NULL,
  payment_date DATE,
  status VARCHAR(15) CHECK (status IN ('aberta','paga','vencida')) DEFAULT 'aberta'
);

-- Recurrences
CREATE TABLE recurrences (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  type VARCHAR(10) CHECK (type IN ('receita','despesa')) NOT NULL,
  description VARCHAR(150) NOT NULL,
  amount NUMERIC(15,2) NOT NULL,
  category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
  account_id UUID REFERENCES accounts(id) ON DELETE SET NULL,
  frequency VARCHAR(10) CHECK (frequency IN ('semanal','mensal','anual')) NOT NULL,
  due_day INTEGER NOT NULL CHECK (due_day BETWEEN 1 AND 31),
  start_date DATE NOT NULL,
  end_date DATE,
  next_generation DATE,
  last_generated_at TIMESTAMP WITH TIME ZONE,
  active BOOLEAN DEFAULT TRUE,
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Budgets
CREATE TABLE budgets (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  group_id UUID REFERENCES family_groups(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  category_id UUID REFERENCES categories(id) ON DELETE CASCADE,
  year INTEGER NOT NULL,
  month INTEGER NOT NULL CHECK (month BETWEEN 1 AND 12),
  limit_amount NUMERIC(15,2) NOT NULL,
  spent_amount NUMERIC(15,2) NOT NULL DEFAULT 0,
  alert_percentage NUMERIC(5,2
